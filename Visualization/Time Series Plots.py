import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv('path_to_your_data.csv')

# Display first few rows of the dataset
data.head()
# Set the index to a datetime column if available, otherwise create one
# Assuming 'datetime' column is available in your dataset
data['datetime'] = pd.to_datetime(data[['year', 'month', 'day', 'hour']])  # Adjust as per your data
data.set_index('datetime', inplace=True)

# Plot Time Series for Air Quality Metrics
plt.figure(figsize=(15, 10))

# Plot O3
plt.subplot(3, 3, 1)
plt.plot(data.index, data['O3 (ppb)'], color='blue')
plt.title('O3 (ppb) Over Time')
plt.ylabel('O3 (ppb)')
plt.xlabel('Date')

# Plot PM1
plt.subplot(3, 3, 2)
plt.plot(data.index, data['PM1 (µg/m³)'], color='red')
plt.title('PM1 (µg/m³) Over Time')
plt.ylabel('PM1 (µg/m³)')
plt.xlabel('Date')

# Plot PM2.5
plt.subplot(3, 3, 3)
plt.plot(data.index, data['PM2.5 (µg/m³)'], color='green')
plt.title('PM2.5 (µg/m³) Over Time')
plt.ylabel('PM2.5 (µg/m³)')
plt.xlabel('Date')

# Plot PM4
plt.subplot(3, 3, 4)
plt.plot(data.index, data['PM4 (µg/m³)'], color='purple')
plt.title('PM4 (µg/m³) Over Time')
plt.ylabel('PM4 (µg/m³)')
plt.xlabel('Date')

# Plot PM10
plt.subplot(3, 3, 5)
plt.plot(data.index, data['PM10 (µg/m³)'], color='orange')
plt.title('PM10 (µg/m³) Over Time')
plt.ylabel('PM10 (µg/m³)')
plt.xlabel('Date')

# Plot CO
plt.subplot(3, 3, 6)
plt.plot(data.index, data['CO (ppm)'], color='cyan')
plt.title('CO (ppm) Over Time')
plt.ylabel('CO (ppm)')
plt.xlabel('Date')

# Plot NO
plt.subplot(3, 3, 7)
plt.plot(data.index, data['NO (ppb)'], color='magenta')
plt.title('NO (ppb) Over Time')
plt.ylabel('NO (ppb)')
plt.xlabel('Date')

# Plot NO2
plt.subplot(3, 3, 8)
plt.plot(data.index, data['NO2 (ppb)'], color='brown')
plt.title('NO2 (ppb) Over Time')
plt.ylabel('NO2 (ppb)')
plt.xlabel('Date')

plt.tight_layout()
plt.show()

# Plot Time Series for Weather and Traffic Metrics
plt.figure(figsize=(15, 10))

# Plot Traffic Flow
plt.subplot(3, 3, 1)
plt.plot(data.index, data['Traffic Flow (Passenger Car Units)'], color='blue')
plt.title('Traffic Flow Over Time')
plt.ylabel('Passenger Car Units')
plt.xlabel('Date')

# Plot Average Speed
plt.subplot(3, 3, 2)
plt.plot(data.index, data['Average Speed (KmPH)'], color='red')
plt.title('Average Speed Over Time')
plt.ylabel('KmPH')
plt.xlabel('Date')

# Plot Rain Duration
plt.subplot(3, 3, 3)
plt.plot(data.index, data['Rain Duration (h)'], color='green')
plt.title('Rain Duration Over Time')
plt.ylabel('Hours')
plt.xlabel('Date')

# Plot Solar Radiation
plt.subplot(3, 3, 4)
plt.plot(data.index, data['Solar Radiation (w/m²)'], color='purple')
plt.title('Solar Radiation Over Time')
plt.ylabel('w/m²')
plt.xlabel('Date')

# Plot Wind Direction
plt.subplot(3, 3, 5)
plt.plot(data.index, data['Wind Direction (degrees)'], color='orange')
plt.title('Wind Direction Over Time')
plt.ylabel('Degrees')
plt.xlabel('Date')

# Plot Max Wind Speed
plt.subplot(3, 3, 6)
plt.plot(data.index, data['Max Wind Speed (m/h)'], color='cyan')
plt.title('Max Wind Speed Over Time')
plt.ylabel('m/h')
plt.xlabel('Date')

plt.tight_layout()
plt.show()
