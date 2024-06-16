# Mastering Python: Data Manipulation with Pandas - Introduction to Time Series Data

## Overview
This tutorial covers the basics of working with time series data using Pandas. You'll learn how to handle, analyze, and visualize time series data, which is essential for various fields such as finance, economics, and environmental science.

## Table of Contents
1. [Understanding Time Series Data](#understanding-time-series-data)
2. [Creating and Manipulating Time Series Data with Pandas](#creating-and-manipulating-time-series-data-with-pandas)
3. [Indexing and Slicing Time Series Data](#indexing-and-slicing-time-series-data)
4. [Resampling Time Series Data](#resampling-time-series-data)
5. [Rolling and Expanding Windows](#rolling-and-expanding-windows)
6. [Plotting Time Series Data](#plotting-time-series-data)
7. [About BotCampus AI](#about-botcampus-ai)

## Understanding Time Series Data

**What is Time Series Data?**
Time series data is a sequence of data points indexed in time order. It's used in various applications where data is recorded at regular intervals, such as stock prices, weather data, and sensor readings.

**Key Characteristics of Time Series Data:**
1. **Temporal Ordering:** The data points in time series data are ordered chronologically.
2. **Regular Intervals:** The data is often collected at regular time intervals (e.g., daily, monthly, yearly).
3. **Trends and Seasonality:** Time series data often exhibits trends and seasonal patterns.

## Creating and Manipulating Time Series Data with Pandas

**Creating a Time Series:**
Pandas provides powerful tools for working with time series data. You can create a simple time series by generating a date range and random data.

**Code Example: Creating a Time Series**
```python
import pandas as pd
import numpy as np

# Creating a date range
date_range = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
print("Date Range:\n", date_range)

# Creating a time series with random data
time_series = pd.Series(np.random.randn(len(date_range)), index=date_range)
print("\nTime Series:\n", time_series)
```

## Indexing and Slicing Time Series Data

**Indexing and Slicing:**
You can easily index and slice time series data using Pandas' powerful indexing capabilities.

**Code Example: Indexing and Slicing Time Series**
```python
# Indexing a specific date
print("\nValue on 2023-01-03:", time_series['2023-01-03'])

# Slicing a range of dates
print("\nTime Series from 2023-01-03 to 2023-01-07:\n", time_series['2023-01-03':'2023-01-07'])
```

## Resampling Time Series Data

**Resampling:**
Resampling involves changing the frequency of your time series data. You can aggregate data to a higher level (downsampling) or interpolate data to a lower level (upsampling).

**Code Example: Resampling Time Series**
```python
# Resampling to monthly frequency and calculating the mean
monthly_resampled = time_series.resample('M').mean()
print("\nMonthly Resampled Time Series:\n", monthly_resampled)

# Resampling to hourly frequency and forward filling missing values
hourly_resampled = time_series.resample('H').ffill()
print("\nHourly Resampled Time Series:\n", hourly_resampled)
```

## Rolling and Expanding Windows

**Rolling and Expanding Windows:**
Rolling and expanding windows are used to calculate statistics over a specified window or expanding range of time.

**Code Example: Rolling and Expanding Windows**
```python
# Calculating a rolling mean with a window of 3 days
rolling_mean = time_series.rolling(window=3).mean()
print("\nRolling Mean (3-day window):\n", rolling_mean)

# Calculating an expanding mean
expanding_mean = time_series.expanding().mean()
print("\nExpanding Mean:\n", expanding_mean)
```

## Plotting Time Series Data

**Visualizing Time Series Data:**
Visualizing time series data is crucial for understanding trends and patterns. Pandas integrates well with Matplotlib for plotting.

**Code Example: Plotting Time Series**
```python
import matplotlib.pyplot as plt

# Plotting the original time series
time_series.plot(title='Original Time Series')
plt.show()

# Plotting the rolling mean
rolling_mean.plot(title='Rolling Mean (3-day window)')
plt.show()

# Plotting the expanding mean
expanding_mean.plot(title='Expanding Mean')
plt.show()
```

## About BotCampus AI

**BotCampus AI** is a leading provider of AI and machine learning education. Our mission is to empower individuals and organizations with the knowledge and skills needed to thrive in the AI-driven world.

### Learning Management System
Access our LMS portal at [learn.botcampus.ai](https://learn.botcampus.ai) for more courses and resources.

### Contact Us
- **Website:** [www.botcampus.ai](https://www.botcampus.ai)
- **Email:** support@botcampus.ai
- **GitHub:** [BotCampus AI on GitHub](https://github.com/Bot-Campus-AI/advanced-python)

Thank you for using this project to enhance your Python journey with BotCampus AI. Enjoy coding!

© 2024 BotCampus AI. All rights reserved.