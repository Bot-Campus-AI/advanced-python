# Working with Pandas DataFrames

## Overview
This tutorial covers the basics of working with Pandas DataFrames, including creating DataFrames, accessing data, and performing basic operations. DataFrames are the core data structure in Pandas, essential for data manipulation and analysis.

## Table of Contents
1. [Understanding DataFrames](#understanding-dataframes)
2. [Creating DataFrames](#creating-dataframes)
3. [Accessing Data in DataFrames](#accessing-data-in-dataframes)
4. [Basic Operations on DataFrames](#basic-operations-on-dataframes)
5. [Summary](#summary)
6. [About BotCampus AI](#about-botcampus-ai)

## Understanding DataFrames
A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. It's similar to a table in a database or an Excel spreadsheet. DataFrames are incredibly versatile and are the primary data structure you'll be working with in Pandas.

**Key Characteristics of DataFrames:**
1. **Labeled Axes:** DataFrames have labeled axes (rows and columns), which makes it easy to refer to data by column name or row index.
2. **Heterogeneous Data:** Each column in a DataFrame can contain different types of data, such as integers, floats, strings, and more.
3. **Size-Mutable:** DataFrames can be resized by adding or removing rows and columns.

## Creating DataFrames

### Creating a DataFrame from a Dictionary
One of the most common ways to create a DataFrame is from a dictionary, where the keys are column names and the values are lists of column data.

```python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)
print("DataFrame from dictionary:\n", data_frame)
```

### Creating a DataFrame from a List of Lists
You can also create a DataFrame from a list of lists, specifying the column names separately.

```python
import pandas as pd

# Creating a DataFrame from a list of lists
data = [
    ['Raj', 30, 'Delhi'],
    ['Amit', 25, 'Mumbai'],
    ['Priya', 35, 'Bangalore']
]
columns = ['Name', 'Age', 'City']
data_frame = pd.DataFrame(data, columns=columns)
print("DataFrame from list of lists:\n", data_frame)
```

## Accessing Data in DataFrames

### Accessing Columns
You can access columns in a DataFrame using the column name. This can be done using the bracket notation or dot notation.

```python
# Accessing columns using bracket notation
print("Names column:\n", data_frame['Name'])

# Accessing columns using dot notation
print("Ages column:\n", data_frame.Age)
```

### Accessing Rows
You can access rows in a DataFrame using the `loc` and `iloc` properties. `loc` is label-based, while `iloc` is integer position-based.

```python
# Accessing rows using loc
print("First row using loc:\n", data_frame.loc[0])

# Accessing rows using iloc
print("Second row using iloc:\n", data_frame.iloc[1])
```

## Basic Operations on DataFrames

### Adding and Removing Columns
You can easily add or remove columns in a DataFrame.

```python
# Adding a new column
data_frame['Country'] = ['India', 'India', 'India']
print("DataFrame with new column:\n", data_frame)

# Removing a column
data_frame = data_frame.drop('Country', axis=1)
print("DataFrame after removing column:\n", data_frame)
```

### Filtering Data
You can filter data in a DataFrame based on specific conditions.

```python
# Filtering rows where Age is greater than 30
filtered_df = data_frame[data_frame['Age'] > 30]
print("Filtered DataFrame:\n", filtered_df)
```

## Summary
In this tutorial, we explored Pandas DataFrames in detail. We learned what DataFrames are, how to create them from dictionaries and lists, and how to perform basic operations like accessing and modifying data, and filtering data. Understanding these basics is crucial for working with data in Python.

## About BotCampus AI
**BotCampus AI** is a leading provider of AI and machine learning education. Our mission is to empower individuals and organizations with the knowledge and skills needed to thrive in the AI-driven world.

### Learning Management System
Access our LMS portal at [learn.botcampus.ai](https://learn.botcampus.ai) for more courses and resources.

### Contact Us
- **Website:** [www.botcampus.ai](https://www.botcampus.ai)
- **Email:** support@botcampus.ai
- **GitHub:** [BotCampus AI on GitHub](https://github.com/Bot-Campus-AI/advanced-python)

---

Thank you for choosing this project to enhance your Python skills with BotCampus AI. Happy coding!

---

All rights reserved.