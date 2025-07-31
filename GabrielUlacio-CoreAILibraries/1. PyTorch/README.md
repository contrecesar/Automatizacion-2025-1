# Temperature Prediction with PyTorch

Predict daily temperatures for the next N days using LSTM neural networks.

## Features

- Data preprocessing and normalization
- LSTM model implementation
- Training pipeline
- Prediction visualization


## Data

Place your weather data in the `data` folder as a CSV file. The dataset used for this project was extracted from [Visual Crossing Weather](https://www.visualcrossing.com/weather-query-builder/#).

If you want to try predictions for another city, use Visual Crossing to download the weather data for your desired location. Make sure your CSV contains all the columns required by `predict.py` and `train.py` (e.g., date, temperature, and any other features used in the scripts).

## Installation

1. Clone the repository
```bash
git clone https://github.com/tu-usuario/temperature-prediction-pytorch.git
```
2. Create and activate environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```

## Usage
1. Train the model:
```bash
python src/models/train.py
```
2. Make predictions:
```bash
python src/models/predict.py
```
