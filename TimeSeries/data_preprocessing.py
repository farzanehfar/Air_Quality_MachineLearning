import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    df.reset_index(drop=True, inplace=True)
    
    tf = df['Traffic Flow'].values
    df['two wheeled motor vehicles'] = tf * 0.0063
    df['cars and taxis'] = tf * 0.8
    df['buses and coaches'] = tf * 0.0124
    df['lgvs'] = tf * 0.1813
    
    df = df.drop(['Traffic Flow', 'Congestion', 'hour'], axis=1)
    
    labels = df['NO2'].values
    df['NO2'] = set_tags_no2(labels)
    df.fillna(0, inplace=True)

    return df

def set_tags_no2(labels):
    templ = np.array(labels, dtype='object')
    for i in range(len(labels)):
        if labels[i] > 200:
            templ[i] = 'Very unhealthy'
        elif labels[i] <= 200 and labels[i] > 150:
            templ[i] = 'Unhealthy'
        elif labels[i] <= 150 and labels[i] > 100:
            templ[i] = 'Unhealthy for sensitive group'
        elif labels[i] <= 100 and labels[i] > 50:
            templ[i] = 'Moderate'
        else:
            templ[i] = 'Good'
    return templ

if __name__ == "__main__":
    file_path = 'data/mix2018.csv'
    processed_data = preprocess_data(file_path)
    processed_data.to_csv('data/processed_data.csv', index=False)
    print("Data preprocessing completed and saved to 'data/processed_data.csv'.")

