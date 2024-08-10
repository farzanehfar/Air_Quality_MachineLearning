# Air Quality & Machine Learning Using Classification and Time-Series Methods

This repository contains the code and data for the following publications on air quality and machine learning:

## Publications
1. **Machine Learning for Transport Policy Interventions on Air Quality**  
   Published in IEEE Access, 2023  
   [Access the publication](https://ieeexplore.ieee.org/document/10114913)  
   
   ```bibtex
   @article{farhadi2023machine,
     title={Machine Learning for Transport Policy Interventions on Air Quality},
     author={Farhadi, Farzaneh and Palacin, Roberto and Blythe, Phil},
     journal={IEEE Access},
     year={2023},
     publisher={IEEE}
   }
   
2. **Data-driven framework for validating policies: Air quality case study**
Published in the 2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC)
 [Access the publication](https://ieeexplore.ieee.org/abstract/document/9922587)

 ```bibtex
@inproceedings{farhadi2022data,
  title={Data-driven framework for validating policies: Air quality case study},
  author={Farhadi, Farzaneh and Palacin, Roberto and Blythe, Phil},
  booktitle={2022 IEEE 25th International Conference on Intelligent Transportation Systems (ITSC)},
  pages={237--243},
  year={2022},
  organization={IEEE}
}
```

# Data Source 
The data used in this project can be downloaded from the Newcastle Urban Observatory. We utilized air quality data for the year 2018, which can be accessed from the following link:

[Download Data](https://newcastle.urbanobservatory.ac.uk/data/agg/3600/years/2018)
Instructions for Downloading the Data:
1. Visit the link: Newcastle Urban Observatory Data
2. Select the desired parameters: On the webpage, you can choose specific parameters such as pollutants, and time intervals if necessary.
3. Download the data: After setting your parameters, click on the download button to obtain the CSV file(s).

Note:
Ensure that the data is saved in the data/ directory of this repository with the correct filename, so that the provided code can correctly access and process the data.

# Project Structure
This repository is organized into the following sections:

1. Preprocessing (Data Cleaning)
This module is responsible for cleaning and preparing the raw air quality data for analysis. It includes:

## a) Handling Missing Values: Missing values in the dataset are handled appropriately, either through imputation or removal, depending on the context.
## b) Normalization/Standardization: The data is normalized or standardized to ensure consistency across different features.
## c) Feature Engineering: Additional features are created to enhance the predictive power of the models.

2. Visualization
In this section, the cleaned data is visualized to identify patterns, trends, and anomalies. The following types of plots and graphs are generated:

a) Time Series Plots: Visualize changes in air quality over time.
b) Histograms: Examine the distribution of air quality levels.

3. Classification
This module applies machine learning classification algorithms to predict air quality levels based on the preprocessed data. The steps include:

a) Data Splitting: The data is split into training and testing sets.
b) Model Training: Various classification models (e.g., Decision Trees, SVM, Random Forest) are trained on the training data.
c) Model Evaluation: The models are evaluated on the test data using metrics such as accuracy, precision, recall, and F1-score.
d) Model Comparison: Performance metrics of different models are compared to select the best-performing model.

4. Time Series Analysis
Time series models are applied to predict future air quality levels based on historical data. This section includes:

a) Model Selection: Time series models such as LSTM is selected based on the data characteristics.
b) Training and Validation: The selected models are trained on historical data and validated using a portion of the dataset.
c) Forecasting: The trained models are used to predict future air quality trends, and their performance is evaluated.

