
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler


def load_and_clean_data(filepath):
    """
    Loads and cleans temperature data. Returns cleaned DataFrame and scaler.
    """
    df = pd.read_csv(filepath)[['datetime', 'temp']]
    df['datetime'] = pd.to_datetime(df['datetime'])
    df = df.sort_values('datetime')
    if df['temp'].isnull().any():
        df['temp'] = df['temp'].interpolate()
    scaler = MinMaxScaler()
    df['temp_normalized'] = scaler.fit_transform(df[['temp']])
    return df, scaler



def create_sequences(data, sequence_length):
    """
    Returns X, y arrays for LSTM training.
    """
    X = [data[i:i+sequence_length] for i in range(len(data) - sequence_length)]
    y = [data[i+sequence_length] for i in range(len(data) - sequence_length)]
    return np.array(X), np.array(y)



#filepath = "data/San Cristóbal 2024-07-01 to 2025-07-01.csv"

#df, scaler = load_and_clean_data(filepath)

#sequence_length = 5
#X, y = create_sequences(df['temp_normalized'].values, sequence_length)

