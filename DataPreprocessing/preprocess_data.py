import os
import pandas as pd

def preprocess_csv_files(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            size_filename = len(filename)
            filename_short = filename[:size_filename - 4].replace(".", "_")
            
            path_main = os.path.join(input_dir, filename)
            path_avg = os.path.join(output_dir, f"{filename_short}_avg.csv")
            
            print(f"Processing {filename}...")
            
            # Read the original dataset
            dataset = pd.read_csv(path_main)
            
            # Convert timestamp to datetime and extract year, month, day, hour
            dataset["datetime"] = pd.to_datetime(dataset["timestamp"])
            dataset["year"] = dataset["datetime"].dt.year
            dataset["month"] = dataset["datetime"].dt.month
            dataset["day"] = dataset["datetime"].dt.day
            dataset["hour"] = dataset["datetime"].dt.hour
            
            # Calculate hourly mean
            datasethourlymean = dataset.groupby(["year", "month", "day", "hour"]).value.mean()
            
            # Save the processed dataset
            datasethourlymean.to_csv(path_avg, index=True, header=True)
            datasetavg = pd.read_csv(path_avg)
            datasetavg.rename(columns={'value': filename_short}, inplace=True)
            datasetavg.to_csv(path_avg, index=False)

if __name__ == "__main__":
    input_dir = '../DataPreprocessing/data/raw_data'
    output_dir = '../DataPreprocessing/data/processed_data'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    preprocess_csv_files(input_dir, output_dir)
    print("Preprocessing completed.")
