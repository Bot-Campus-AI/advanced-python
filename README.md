# Mastering Python: Data Manipulation with Pandas - Aggregating and Grouping Data

## Overview
This tutorial covers the basics of aggregating and grouping data using Pandas. You'll learn how to use Pandas to group data and perform various aggregation functions. These techniques are essential for summarizing and analyzing large datasets.

## Table of Contents
1. [Understanding Aggregation and Grouping](#understanding-aggregation-and-grouping)
2. [Aggregating Data](#aggregating-data)
3. [Grouping Data](#grouping-data)
4. [Applying Multiple Aggregation Functions](#applying-multiple-aggregation-functions)
5. [Grouping by Multiple Columns](#grouping-by-multiple-columns)
6. [Using `transform` for Group-Wise Operations](#using-transform-for-group-wise-operations)
7. [About BotCampus AI](#about-botcampus-ai)

## Understanding Aggregation and Grouping

**What is Aggregation?**
Aggregation involves summarizing data by applying functions like sum, mean, count, etc. It's useful for deriving insights from large datasets.

**What is Grouping?**
Grouping involves splitting the data into groups based on some criteria and then applying aggregation functions to each group. This is particularly useful for comparing different subsets of the data.

## Aggregating Data

**Basic Aggregation Functions:**
Pandas provides several built-in functions for aggregation, such as `sum`, `mean`, `min`, `max`, and `count`.

**Code Example: Basic Aggregation Functions**
```python
import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Amit', 'Raj', 'Priya'],
    'Age': [30, 25, 35, 28, 32, 38],
    'Salary': [70000, 80000, 75000, 85000, 72000, 77000]
}
data_frame = pd.DataFrame(data)
print("DataFrame:\n", data_frame)

# Applying aggregation functions
total_salary = data_frame['Salary'].sum()
average_age = data_frame['Age'].mean()
max_salary = data_frame['Salary'].max()

print("\nTotal Salary:", total_salary)
print("Average Age:", average_age)
print("Maximum Salary:", max_salary)
```

## Grouping Data

**Grouping Data with `groupby`:**
The `groupby` method in Pandas is used to split the data into groups based on one or more columns.

**Code Example: Grouping Data**
```python
# Grouping data by Name
grouped_data = data_frame.groupby('Name')

# Aggregating data within each group
mean_salary = grouped_data['Salary'].mean()
total_salary = grouped_data['Salary'].sum()

print("\nMean Salary by Name:\n", mean_salary)
print("\nTotal Salary by Name:\n", total_salary)
```

## Applying Multiple Aggregation Functions

**Multiple Aggregations:**
You can apply multiple aggregation functions to a group using the `agg` method.

**Code Example: Applying Multiple Aggregations**
```python
# Applying multiple aggregation functions
agg_data = grouped_data['Salary'].agg(['mean', 'sum', 'max'])
print("\nMultiple Aggregations on Salary:\n", agg_data)
```

## Grouping by Multiple Columns

**Grouping by Multiple Columns:**
You can group data by multiple columns to create more detailed summaries.

**Code Example: Grouping by Multiple Columns**
```python
# Grouping data by Name and Age
multi_grouped_data = data_frame.groupby(['Name', 'Age'])

# Aggregating data within each group
multi_agg_data = multi_grouped_data['Salary'].sum()
print("\nTotal Salary by Name and Age:\n", multi_agg_data)
```

## Using `transform` for Group-Wise Operations

**Using `transform`:**
The `transform` method allows you to perform group-wise operations and return a DataFrame with the same shape as the original.

**Code Example: Using `transform`**
```python
# Adding a column for mean salary by group
data_frame['Mean Salary by Name'] = data_frame.groupby('Name')['Salary'].transform('mean')
print("\nDataFrame with Mean Salary by Name:\n", data_frame)
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