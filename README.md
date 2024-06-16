# Time Series Visualization with Pandas and Matplotlib

## Overview
This tutorial covers time series visualization using Pandas and Matplotlib. By the end of this tutorial, you will understand how to create various types of time series plots to effectively communicate data insights, including basic plots, customized plots, multiple series plots, highlighted periods, rolling statistics, and seasonal decomposition.

## Table of Contents
1. [Importance of Time Series Visualization](#importance-of-time-series-visualization)
2. [Basic Time Series Plot](#basic-time-series-plot)
3. [Customizing Time Series Plots](#customizing-time-series-plots)
4. [Plotting Multiple Time Series](#plotting-multiple-time-series)
5. [Highlighting Specific Time Periods](#highlighting-specific-time-periods)
6. [Plotting Rolling Statistics](#plotting-rolling-statistics)
7. [Plotting Seasonal Decomposition](#plotting-seasonal-decomposition)
8. [About BotCampus AI](#about-botcampus-ai)

## Importance of Time Series Visualization

**Why Visualize Time Series Data?**
Visualizing time series data helps identify trends, seasonal patterns, and outliers, allowing you to convey complex temporal relationships simply and intuitively.

## Basic Time Series Plot

**Creating a Basic Time Series Plot:**
Start by creating a basic time series plot using Pandas and Matplotlib.

**Code Example: Basic Time Series Plot**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
print("Original Time Series:\n", time_series)

# Plotting the time series
time_series.plot(title='Basic Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
```

## Customizing Time Series Plots

**Customizing Plots:**
Customize your time series plots by adding gridlines, changing colors, and using different line styles.

**Code Example: Customizing Time Series Plots**
```python
# Customizing the plot
time_series.plot(title='Customized Time Series Plot', color='green', linestyle='--', marker='o')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
```

## Plotting Multiple Time Series

**Plotting Multiple Time Series:**
Plot multiple time series on the same graph to compare different data sets.

**Code Example: Plotting Multiple Time Series**
```python
# Creating another time series
time_series_1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
time_series_2 = pd.Series([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index=date_range)

# Plotting multiple time series
plt.figure()
time_series_1.plot(label='Series 1')
time_series_2.plot(label='Series 2')
plt.title('Multiple Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
```

## Highlighting Specific Time Periods

**Highlighting Specific Periods:**
Highlight specific periods in your time series plot to emphasize certain events or trends.

**Code Example: Highlighting Specific Periods**
```python
# Plotting the time series
plt.figure()
time_series.plot(label='Original Series')
plt.axvspan('2024-01-04', '2024-01-06', color='red', alpha=0.3)
plt.title('Time Series with Highlighted Period')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
```

## Plotting Rolling Statistics

**Plotting Rolling Statistics:**
Rolling statistics, such as the rolling mean or rolling standard deviation, are useful for smoothing out short-term fluctuations and highlighting longer-term trends.

**Code Example: Plotting Rolling Statistics**
```python
# Calculating rolling mean
rolling_mean = time_series.rolling(window=3).mean()

# Plotting original series and rolling mean
plt.figure()
time_series.plot(label='Original Series')
rolling_mean.plot(label='Rolling Mean (3-day window)')
plt.title('Time Series with Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()
```

## Plotting Seasonal Decomposition

**Seasonal Decomposition:**
Seasonal decomposition involves breaking down a time series into its trend, seasonal, and residual components.

**Code Example: Seasonal Decomposition**
```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Creating a sample time series with seasonality
date_range = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
time_series = pd.Series([i + (5 * (i % 7)) for i in range(len(date_range))], index=date_range)

# Decomposing the time series
decomposition = seasonal_decompose(time_series, model='additive')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plotting the decomposition
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(time_series, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='best')
plt.tight_layout()
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