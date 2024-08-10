import numpy as np
import matplotlib.pyplot as plt
from model_training import train_models
import pandas as pd
from sklearn.model_selection import train_test_split

def permutation_importance(model, X, y, n_repeats=10):
    """Calculate importance score for each feature."""
    importances = []
    for i in range(X.shape[1]):
        score = model.score(X, y)
        X_permuted = X.copy()
        np.random.shuffle(X_permuted[:, i])
        score_permuted = model.score(X_permuted, y)
        importances.append(score - score_permuted)
    return np.array(importances)

def plot_feature_importance(importances, feature_names):
    sorted_idx = np.argsort(importances)
    plt.barh(np.array(feature_names)[sorted_idx], importances[sorted_idx], color='blue')
    plt.xlabel("Feature Importance")
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv('data/processed_data.csv')
    X = data.drop('NO2', axis=1).values
    y = data['NO2'].apply(lambda x: ['Good', 'Moderate', 'Unhealthy for sensitive group', 'Unhealthy', 'Very unhealthy'].index(x)).values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=300)
    models = train_models(X_train, y_train)
    
    model = models['LGBM']
    importances = permutation_importance(model, X_train, y_train)
    plot_feature_importance(importances, data.drop('NO2', axis=1).columns)

