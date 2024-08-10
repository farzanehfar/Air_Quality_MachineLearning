import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from model_training import train_models

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
    print(f"Precision: {precision_score(y_test, y_pred, average=None)}")
    print(f"Recall: {recall_score(y_test, y_pred, average=None)}")
    print(f"F1 Score: {f1_score(y_test, y_pred, average=None)}")
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test)
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/processed_data.csv')
    X = data.drop('NO2', axis=1).values
    y = data['NO2'].apply(lambda x: ['Good', 'Moderate', 'Unhealthy for sensitive group', 'Unhealthy', 'Very unhealthy'].index(x)).values

    X_train, X_test, y_train, y_test =
