import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

def train_lstm_model(X_train, y_train, X_test, y_test):
    model = Sequential()
    model.add(LSTM(200, input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer='sgd')

    history = model.fit(X_train, y_train, epochs=500, validation_data=(X_test, y_test), batch_size=1, verbose=2, shuffle=True)
    
    return model, history

if __name__ == "__main__":
    df = pd.read_csv('data/processed_data.csv')
    X = df.drop('NO2', axis=1).values
    y = df['NO2'].values

    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_X = scaler.fit_transform(X)
    X_supervised = series_to_supervised(scaled_X, 1, 1)

    X_train, X_test, y_train, y_test = train_test_split(X_supervised, y[1:], test_size=0.3, random_state=300)

    X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
    X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

    model, history = train_lstm_model(X_train, y_train, X_test, y_test)

    model.save('models/lstm_model.h5')
    print("Model training completed and saved to 'models/lstm_model.h5'.")
