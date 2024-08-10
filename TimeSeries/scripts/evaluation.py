import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

if __name__ == "__main__":
    model = load_model('models/lstm_model.h5')

    df = pd.read_csv('data/processed_data.csv')
    X = df.drop('NO2', axis=1).values
    y = df['NO2'].values

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_X = scaler.fit_transform(X)
    X_supervised = series_to_supervised(scaled_X, 1, 1)
    X_supervised = X_supervised.reshape((X_supervised.shape[0], 1, X_supervised.shape[1]))

    predictions = model.predict(X_supervised)
    rmse = np.sqrt(mean_squared_error(y[1:], predictions))

    print(f"Test RMSE: {rmse:.3f}")
    
    plt.plot(predictions, label='Predicted')
    plt.plot(y[1:], label='True')
    plt.ylabel('NO2 Concentration Class')
    plt.xlabel('Time Samples')
    plt.legend()
    plt.show()
