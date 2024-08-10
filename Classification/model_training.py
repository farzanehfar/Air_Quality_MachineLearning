import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from lightgbm import LGBMClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

def train_models(X_train, y_train):
    models = {
        "LGBM": LGBMClassifier(random_state=1234, num_leaves=31, learning_rate=0.05),
        "DecisionTree": DecisionTreeClassifier(max_depth=10, random_state=1234),
        "KNN": KNeighborsClassifier(n_neighbors=5),
        "GradientBoosting": GradientBoostingClassifier(max_depth=10, learning_rate=0.1, n_estimators=100, random_state=1234)
    }

    for name, model in models.items():
        model.fit(X_train, y_train)
        train_preds = model.predict(X_train)
        accuracy = accuracy_score(y_train, train_preds)
        print(f"{name} Training accuracy: {accuracy*100:.2f}%")

    return models

if __name__ == "__main__":
    data = pd.read_csv('data/processed_data.csv')
    X = data.drop('NO2', axis=1).values
    y = data['NO2'].apply(lambda x: ['Good', 'Moderate', 'Unhealthy for sensitive group', 'Unhealthy', 'Very unhealthy'].index(x)).values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=300)
    models = train_models(X_train, y_train)
    print("Model training completed.")
