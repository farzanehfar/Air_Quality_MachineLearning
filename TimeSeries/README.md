# Time Series Prediction with LSTM for Air Quality Data

This directory contains scripts for time series analysis and prediction using LSTM models on air quality data.

## How to Use

### 1. Install Dependencies

Ensure you have Python installed. Install the required packages by running:

```bash
pip install -r requirements.txt
```
### 2. Prepare the Data
Place your dataset (mix2018.csv) in the data/ directory. If you don't have mix2018.csv ready, preprocess your raw data files:
```bash
python scripts/data_preprocessing.py
```
### 3. Train the LSTM Model
   ```bash
   python scripts/lstm_training.py
   ```
### 4. Evaluate Policy Impact
   ```bash
   python scripts/policy_evaluation.py
   ```
### 5. Evaluate the Models
   ```bash
   python scripts/evaluation.py
   ```
