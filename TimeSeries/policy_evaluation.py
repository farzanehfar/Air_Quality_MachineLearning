import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def policy_intervention_effect(df):
    # Apply your policy intervention here, modifying the dataframe as needed
    df['two wheeled motor vehicles'] *= 0.8
    df['cars and taxis'] *= 0.8
    df['buses and coaches'] *= 0.9
    df['lgvs'] *= 0.8
    df['NO2'] -= 25

    return df

if __name__ == "__main__":
    df = pd.read_csv('data/processed_data.csv')
    model = load_model('models/lstm_model.h5')
    
    df_policy = policy_intervention_effect(df.copy())
    
    X = df_policy.drop('NO2', axis=1).values
    y = df_policy['NO2'].values
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_X = scaler.fit_transform(X)
    X_supervised = series_to_supervised(scaled_X, 1, 1)

    X_supervised = X_supervised.reshape((X_supervised.shape[0], 1, X_supervised.shape[1]))

    predictions = model.predict(X_supervised)
    scaler = MinMaxScaler(feature_range=(0, 4))
    predictions = scaler.fit_transform(predictions)

    plt.plot(predictions, label='Predicted after policy intervention')
    plt.ylabel('NO2 Concentration Class')
    plt.xlabel('Time Samples')
    plt.legend()
    plt.show()
