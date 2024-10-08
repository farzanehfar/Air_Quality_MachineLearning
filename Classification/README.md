# Classification Models for Air Quality Data

This directory contains the scripts for training, evaluating, and analyzing classification models on air quality data.

## How to Use

1. **Install Dependencies**

   Ensure you have Python installed. Install the required packages by running:
   
   ```bash
   pip install -r requirements.txt

2. **Prepare the Data**

 ```bash
Place your dataset (mix2018.csv) in the data/ directory.
 ```

3. **Run the Preprocessing Script**

```bash
python scripts/data_preprocessing.py
 ```

4. **Train the Models**
    ```bash
   python scripts/model_training.py
   ```
6. **Analyze Feature Importance**
    ```bash
   python scripts/feature_importance.py
   ```
7. **Evaluate the Models**
 ```bash
python scripts/evaluation.py
 ```
