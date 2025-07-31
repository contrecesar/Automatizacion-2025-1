
import torch
import numpy as np
import pandas as pd
from utils.data_cleaner import load_and_clean_data
from models.temperature_model import TemperaturePredictor

# Parameters
SEQUENCE_LENGTH = 30  # Must match the training sequence length
DAYS_TO_PREDICT = 3

def predict_future_temperatures(model, scaler, last_sequence, days_to_predict=DAYS_TO_PREDICT):
    model.eval()
    predictions = []
    current_sequence = last_sequence.copy()

    for _ in range(days_to_predict):
        with torch.no_grad():
            input_tensor = torch.FloatTensor(current_sequence).unsqueeze(0).unsqueeze(-1)
            pred = model(input_tensor)
            pred_value = pred.item()
            predictions.append(pred_value)
            # Update sequence
            current_sequence = np.append(current_sequence[1:], pred_value)

    # Denormalize predictions
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    return predictions.flatten()

def main():
    # Load data and model
    df, scaler = load_and_clean_data("data/San Cristóbal 2024-07-01 to 2025-07-01.csv")
    data = df['temp_normalized'].values

    # Get last sequence
    last_sequence = data[-SEQUENCE_LENGTH:]

    # Load model
    model = TemperaturePredictor()
    model.load_state_dict(torch.load('temperature_model.pth'))

    # Predict
    predictions = predict_future_temperatures(model, scaler, last_sequence, days_to_predict=DAYS_TO_PREDICT)

    # Create DataFrame with results
    last_date = df['datetime'].iloc[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=DAYS_TO_PREDICT)
    result_df = pd.DataFrame({
        'Date': future_dates,
        'Predicted Temperature': predictions
    })

    print("\nPredictions for the next 3 days:")
    print(result_df.to_string(index=False))

    # Save results
    result_df.to_csv('predicted_temperature.csv', index=False)

if __name__ == "__main__":
    main()