import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('path_to_your_data.csv')

# Display first few rows of the dataset
data.head()

# Plot Histograms for Air Quality Metrics
plt.figure(figsize=(15, 10))

# Histogram for O3
plt.subplot(3, 3, 1)
sns.histplot(data['O3 (ppb)'], bins=30, kde=True, color='blue')
plt.title('O3 (ppb) Distribution')
plt.xlabel('O3 (ppb)')

# Histogram for PM1
plt.subplot(3, 3, 2)
sns.histplot(data['PM1 (µg/m³)'], bins=30, kde=True, color='red')
plt.title('PM1 (µg/m³) Distribution')
plt.xlabel('PM1 (µg/m³)')

# Histogram for PM2.5
plt.subplot(3, 3, 3)
sns.histplot(data['PM2.5 (µg/m³)'], bins=30, kde=True, color='green')
plt.title('PM2.5 (µg/m³) Distribution')
plt.xlabel('PM2.5 (µg/m³)')

# Histogram for PM4
plt.subplot(3, 3, 4)
sns.histplot(data['PM4 (µg/m³)'], bins=30, kde=True, color='purple')
plt.title('PM4 (µg/m³) Distribution')
plt.xlabel('PM4 (µg/m³)')

# Histogram for PM10
plt.subplot(3, 3, 5)
sns.histplot(data['PM10 (µg/m³)'], bins=30, kde=True, color='orange')
plt.title('PM10 (µg/m³) Distribution')
plt.xlabel('PM10 (µg/m³)')

# Histogram for CO
plt.subplot(3, 3, 6)
sns.histplot(data['CO (ppm)'], bins=30, kde=True, color='cyan')
plt.title('CO (ppm) Distribution')
plt.xlabel('CO (ppm)')

# Histogram for NO
plt.subplot(3, 3, 7)
sns.histplot(data['NO (ppb)'], bins=30, kde=True, color='magenta')
plt.title('NO (ppb) Distribution')
plt.xlabel('NO (ppb)')

# Histogram for NO2
plt.subplot(3, 3, 8)
sns.histplot(data['NO2 (ppb)'], bins=30, kde=True, color='brown')
plt.title('NO2 (ppb) Distribution')
plt.xlabel('NO2 (ppb)')

plt.tight_layout()
plt.show()

# Plot Histograms for Weather and Traffic Metrics
plt.figure(figsize=(15, 10))

# Histogram for Traffic Flow
plt.subplot(3, 3, 1)
sns.histplot(data['Traffic Flow (Passenger Car Units)'], bins=30, kde=True, color='blue')
plt.title('Traffic Flow Distribution')
plt.xlabel('Passenger Car Units')

# Histogram for Average Speed
plt.subplot(3, 3, 2)
sns.histplot(data['Average Speed (KmPH)'], bins=30, kde=True, color='red')
plt.title('Average Speed Distribution')
plt.xlabel('KmPH')

# Histogram for Rain Duration
plt.subplot(3, 3, 3)
sns.histplot(data['Rain Duration (h)'], bins=30, kde=True, color='green')
plt.title('Rain Duration Distribution')
plt.xlabel('Hours')

# Histogram for Solar Radiation
plt.subplot(3, 3, 4)
sns.histplot(data['Solar Radiation (w/m²)'], bins=30, kde=True, color='purple')
plt.title('Solar Radiation Distribution')
plt.xlabel('w/m²')

# Histogram for Wind Direction
plt.subplot(3, 3, 5)
sns.histplot(data['Wind Direction (degrees)'], bins=30, kde=True, color='orange')
plt.title('Wind Direction Distribution')
plt.xlabel('Degrees')

# Histogram for Max Wind Speed
plt.subplot(3, 3, 6)
sns.histplot(data['Max Wind Speed (m/h)'], bins=30, kde=True, color='cyan')
plt.title('Max Wind Speed Distribution')
plt.xlabel('m/h')

plt.tight_layout()
plt.show()
