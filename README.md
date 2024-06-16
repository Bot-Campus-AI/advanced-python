# Mastering Python: Data Manipulation with Pandas - Data Cleaning and Preparation

## Overview
This tutorial covers the basics of data cleaning and preparation using Pandas. You'll learn how to handle missing values, remove duplicates, transform data types, and apply functions to your data. Clean and well-prepared data is essential for accurate analysis and modeling.

## Table of Contents
1. [Importance of Data Cleaning and Preparation](#importance-of-data-cleaning-and-preparation)
2. [Handling Missing Values](#handling-missing-values)
3. [Removing Duplicates](#removing-duplicates)
4. [Transforming Data Types](#transforming-data-types)
5. [Applying Functions to Data](#applying-functions-to-data)
6. [About BotCampus AI](#about-botcampus-ai)

## Importance of Data Cleaning and Preparation

**Why is Data Cleaning Important?**
Data cleaning and preparation is a crucial step in the data analysis process. Raw data often contains errors, missing values, and inconsistencies that can lead to incorrect conclusions. Cleaning the data ensures that our analysis is accurate and reliable.

## Handling Missing Values

**Identifying Missing Values:**
The first step in handling missing values is identifying them. Pandas provides several methods to do this.

**Code Example: Identifying Missing Values**
```python
import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Raj', 'Amit', 'Priya', None],
    'Age': [30, None, 35, 40],
    'City': ['Delhi', 'Mumbai', None, 'Bangalore']
}
data_frame = pd.DataFrame(data)
print("DataFrame with missing values:\n", data_frame)

# Identifying missing values
print("\nMissing values:\n", data_frame.isnull())
```

**Handling Missing Values:**
There are several ways to handle missing values, including dropping them or filling them with a specific value.

**Code Example: Handling Missing Values**
```python
# Dropping rows with missing values
dropped_df = data_frame.dropna()
print("\nDataFrame after dropping missing values:\n", dropped_df)

# Filling missing values with a specific value
filled_df = data_frame.fillna({'Name': 'Unknown', 'Age': 0, 'City': 'Unknown'})
print("\nDataFrame after filling missing values:\n", filled_df)
```

## Removing Duplicates

**Identifying Duplicates:**
Duplicates can skew your analysis results. Identifying and removing duplicates is essential.

**Code Example: Identifying Duplicates**
```python
# Sample data with duplicates
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Raj'],
    'Age': [30, 25, 35, 30],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}
data_frame = pd.DataFrame(data)
print("DataFrame with duplicates:\n", data_frame)

# Identifying duplicates
print("\nDuplicate rows:\n", data_frame.duplicated())
```

**Removing Duplicates:**
Once identified, duplicates can be removed using the `drop_duplicates` method.

**Code Example: Removing Duplicates**
```python
# Removing duplicate rows
deduped_df = data_frame.drop_duplicates()
print("\nDataFrame after removing duplicates:\n", deduped_df)
```

## Transforming Data Types

**Checking Data Types:**
Data types in a DataFrame may need to be transformed for proper analysis. You can check the data types using the `dtypes` attribute.

**Code Example: Checking Data Types**
```python
# Checking data types
print("Data types in DataFrame:\n", data_frame.dtypes)
```

**Converting Data Types:**
Pandas provides several methods to convert data types, such as `astype`.

**Code Example: Converting Data Types**
```python
# Sample data with incorrect data types
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': ['30', '25', '35'],  # Age should be integers
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)
print("DataFrame with incorrect data types:\n", data_frame)

# Converting data types
data_frame['Age'] = data_frame['Age'].astype(int)
print("\nDataFrame after converting data types:\n", data_frame)
```

## Applying Functions to Data

**Using `apply` Method:**
You can apply custom functions to DataFrame columns using the `apply` method.

**Code Example: Applying Functions**
```python
# Applying a custom function to the Age column
data_frame['Age Group'] = data_frame['Age'].apply(lambda x: 'Adult' if x >= 18 else 'Minor')
print("\nDataFrame after applying function:\n", data_frame)
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