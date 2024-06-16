# Rolling and Expanding Windows with Pandas

## Overview
This tutorial covers rolling and expanding windows using Pandas, essential techniques for analyzing time series data. By the end of this tutorial, you will understand how to use rolling and expanding windows to calculate statistics over a sliding window or an expanding range effectively.

## Table of Contents
1. [Understanding Rolling and Expanding Windows](#understanding-rolling-and-expanding-windows)
2. [Rolling Windows](#rolling-windows)
3. [Expanding Windows](#expanding-windows)
4. [Combining Rolling and Expanding Windows with Other Functions](#combining-rolling-and-expanding-windows-with-other-functions)
5. [Visualizing Rolling and Expanding Windows](#visualizing-rolling-and-expanding-windows)
6. [Practical Applications of Rolling and Expanding Windows](#practical-applications-of-rolling-and-expanding-windows)
7. [About BotCampus AI](#about-botcampus-ai)

## Understanding Rolling and Expanding Windows

**What are Rolling and Expanding Windows?**
Rolling and expanding windows are methods to calculate statistics over a specific window of time. Rolling windows calculate statistics within a fixed-size window that slides over the data, while expanding windows calculate statistics over an expanding range of data.

## Rolling Windows

**Using `rolling` for Rolling Windows:**
Rolling windows are used to calculate statistics within a fixed-size window that moves across the data. Let's see how to use the `rolling` method in Pandas.

**Code Example: Rolling Windows**
```python
import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
print("Original Time Series:\n", time_series)

# Calculating the rolling mean with a window of 3 days
rolling_mean = time_series.rolling(window=3).mean()
print("\nRolling Mean (3-day window):\n", rolling_mean)
```

## Expanding Windows

**Using `expanding` for Expanding Windows:**
Expanding windows calculate statistics over an expanding range of data, starting from the first data point and adding one point at a time.

**Code Example: Expanding Windows**
```python
# Calculating the expanding mean
expanding_mean = time_series.expanding().mean()
print("\nExpanding Mean:\n", expanding_mean)
```

## Combining Rolling and Expanding Windows with Other Functions

**Applying Different Functions:**
You can apply various functions like sum, standard deviation, and custom functions with rolling and expanding windows.

**Code Example: Combining Functions**
```python
# Calculating the rolling sum with a window of 3 days
rolling_sum = time_series.rolling(window=3).sum()
print("\nRolling Sum (3-day window):\n", rolling_sum)

# Calculating the expanding standard deviation
expanding_std = time_series.expanding().std()
print("\nExpanding Standard Deviation:\n", expanding_std)
```

## Visualizing Rolling and Expanding Windows

**Plotting Rolling and Expanding Statistics:**
Visualizing the statistics calculated using rolling and expanding windows helps in understanding the trends and patterns in the data.

**Code Example: Plotting Rolling and Expanding Statistics**
```python
import matplotlib.pyplot as plt

# Plotting the original time series
time_series.plot(title='Original Time Series', label='Original')
plt.legend()
plt.show()

# Plotting the rolling mean
rolling_mean.plot(title='Rolling Mean (3-day window)', label='Rolling Mean')
plt.legend()
plt.show()

# Plotting the expanding mean
expanding_mean.plot(title='Expanding Mean', label='Expanding Mean')
plt.legend()
plt.show()
```

## Practical Applications of Rolling and Expanding Windows

**Practical Applications:**
Rolling and expanding windows are widely used in various fields for different purposes. For example, in finance, rolling windows can be used to calculate moving averages to analyze stock prices. In environmental science, expanding windows can be used to analyze cumulative rainfall data over a period of time.

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