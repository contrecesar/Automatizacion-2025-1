import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from utils.data_cleaner import load_and_clean_data, create_sequences
from models.temperature_model import TemperaturePredictor


# Parameters
SEQUENCE_LENGTH = 30
BATCH_SIZE = 16
EPOCHS = 100
LEARNING_RATE = 0.001


def train():
    # Load and prepare data
    df, scaler = load_and_clean_data("data/San Cristóbal 2024-07-01 to 2025-07-01.csv")
    data = df['temp_normalized'].values

    # Create sequences
    X, y = create_sequences(data, SEQUENCE_LENGTH)

    # Convert to PyTorch tensors
    X_tensor = torch.FloatTensor(X).unsqueeze(-1)
    y_tensor = torch.FloatTensor(y).unsqueeze(-1)

    # Create DataLoader
    dataset = TensorDataset(X_tensor, y_tensor)
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    # Initialize model
    model = TemperaturePredictor()
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

    # Training
    for epoch in range(EPOCHS):
        for batch_x, batch_y in dataloader:
            optimizer.zero_grad()
            outputs = model(batch_x)
            loss = criterion(outputs, batch_y)
            loss.backward()
            optimizer.step()

        if (epoch+1) % 10 == 0:
            print(f'Epoch [{epoch+1}/{EPOCHS}], Loss: {loss.item():.4f}')

    # Save model
    torch.save(model.state_dict(), 'temperature_model.pth')
    print("Model trained and saved!")

if __name__ == "__main__":
    train()