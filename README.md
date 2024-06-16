# Resampling and Frequency Conversion with Pandas

## Overview
This tutorial covers resampling and frequency conversion using Pandas, essential techniques for handling time series data. By the end of this tutorial, you will understand how to resample data and convert frequencies using Pandas.

## Table of Contents
1. [Understanding Resampling and Frequency Conversion](#understanding-resampling-and-frequency-conversion)
2. [Downsampling Data](#downsampling-data)
3. [Upsampling Data](#upsampling-data)
4. [Aggregating Data with Custom Functions](#aggregating-data-with-custom-functions)
5. [Time Shifting](#time-shifting)
6. [Frequency Conversion](#frequency-conversion)
7. [About BotCampus AI](#about-botcampus-ai)

## Understanding Resampling and Frequency Conversion

**What is Resampling?**
Resampling involves changing the frequency of your time series data. It can be used to summarize data at different time intervals, such as converting daily data to monthly data.

**Types of Resampling:**
1. **Downsampling:** Reducing the frequency of the data (e.g., converting daily data to monthly data).
2. **Upsampling:** Increasing the frequency of the data (e.g., converting monthly data to daily data).

## Downsampling Data

**Using `resample` for Downsampling:**
Let's start by downsampling our data. We'll convert daily data to monthly data by calculating the mean for each month.

**Code Example: Downsampling Data**
```python
import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
time_series = pd.Series(range(len(date_range)), index=date_range)
print("Original Time Series (Daily):\n", time_series)

# Downsampling to monthly frequency and calculating the mean
monthly_resampled = time_series.resample('M').mean()
print("\nResampled Time Series (Monthly Mean):\n", monthly_resampled)
```

## Upsampling Data

**Using `resample` for Upsampling:**
Now, let's upsample our data. We'll convert monthly data back to daily data, using forward fill to fill in the missing values.

**Code Example: Upsampling Data**
```python
# Upsampling to daily frequency and forward filling missing values
daily_upsampled = monthly_resampled.resample('D').ffill()
print("\nUpsampled Time Series (Daily, Forward Fill):\n", daily_upsampled)
```

## Aggregating Data with Custom Functions

**Custom Aggregation Functions:**
You can also use custom aggregation functions when resampling your data. For example, let's calculate the sum for each month.

**Code Example: Custom Aggregation Functions**
```python
# Downsampling to monthly frequency and calculating the sum
monthly_sum = time_series.resample('M').sum()
print("\nResampled Time Series (Monthly Sum):\n", monthly_sum)
```

## Time Shifting

**Time Shifting:**
Pandas allows you to shift your time series data forward or backward. This can be useful for comparing data across different time periods.

**Code Example: Time Shifting**
```python
# Shifting data forward by one month
shifted_forward = monthly_resampled.shift(1)
print("\nTime Series Shifted Forward by One Month:\n", shifted_forward)

# Shifting data backward by one month
shifted_backward = monthly_resampled.shift(-1)
print("\nTime Series Shifted Backward by One Month:\n", shifted_backward)
```

## Frequency Conversion

**Converting Frequencies:**
Pandas makes it easy to convert between different time frequencies. For example, let's convert our daily data to business day frequency.

**Code Example: Frequency Conversion**
```python
# Converting to business day frequency
business_day_resampled = time_series.asfreq('B')
print("\nResampled Time Series (Business Day Frequency):\n", business_day_resampled)
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