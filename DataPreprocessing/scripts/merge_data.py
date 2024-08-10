import os
import pandas as pd

def merge_processed_files(input_dir, output_file):
    files_to_merge = [f for f in os.listdir(input_dir) if f.endswith('_avg.csv')]
    
    if not files_to_merge:
        print("No processed files found to merge.")
        return
    
    print(f"Merging {len(files_to_merge)} files...")
    
    # Start with the first file
    path_first = os.path.join(input_dir, files_to_merge[0])
    mix = pd.read_csv(path_first)
    
    # Merge each subsequent file
    for filename in files_to_merge[1:]:
        path_avg = os.path.join(input_dir, filename)
        next_file = pd.read_csv(path_avg)
        mix = pd.merge(next_file, mix, how='inner', on=['year', 'month', 'day', 'hour'])
    
    # Save the merged dataset
    mix.to_csv(output_file, index=False)
    print(f"Data merged and saved to {output_file}")

if __name__ == "__main__":
    input_dir = '../DataPreprocessing/data/processed_data'
    output_file = '../DataPreprocessing/data/mix2018.csv'
    
    merge_processed_files(input_dir, output_file)
    mix = pd.read_csv(output_file)
    display(mix)
