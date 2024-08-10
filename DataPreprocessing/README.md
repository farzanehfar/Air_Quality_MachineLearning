# Data Preprocessing for Air Quality Data

This directory contains scripts for preprocessing raw CSV files and merging them into a single file for further analysis.

## How to Use

1. **Install Dependencies**

   Ensure you have Python installed. Install the required packages by running:
   
   ```bash
   pip install -r requirements.txt
 

2. **Prepare the Data**

    Place your raw downloaded dataset files (CSV) in the data/raw_data/ directory.


3. **Run the Preprocessing Script**

   Preprocess and calculate hourly averages for each dataset:
   
   ```bash
   python scripts/preprocess_data.py
   ```
4. **Merge the Processed Files**

   Merge all preprocessed files into a single file (mix2018.csv):
   
   ```bash
   python scripts/merge_data.py
