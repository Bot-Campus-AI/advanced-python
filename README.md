# Working with Text Data in Pandas

## Overview
This tutorial explores how to work with text data using Pandas. Handling text data is crucial for many data analysis tasks, including cleaning, transforming, and extracting information from textual information. By the end of this tutorial, you will understand how to efficiently work with text data in Pandas.

## Table of Contents
1. [Understanding Text Data](#understanding-text-data)
2. [Practical Applications of Text Data Handling](#practical-applications-of-text-data-handling)
3. [Loading and Inspecting Text Data](#loading-and-inspecting-text-data)
4. [Cleaning Text Data](#cleaning-text-data)
5. [Extracting Information from Text Data](#extracting-information-from-text-data)
6. [Manipulating Text Data](#manipulating-text-data)
7. [Applying Functions to Text Data](#applying-functions-to-text-data)
8. [About BotCampus AI](#about-botcampus-ai)

## Understanding Text Data

### What is Text Data?
Text data consists of strings or sequences of characters. It can include anything from names and addresses to entire documents. Working with text data involves various tasks such as cleaning, manipulation, and extraction.

**Examples:**
- Names
- Addresses
- Text documents

## Practical Applications of Text Data Handling

### Practical Applications
Handling text data is essential in various real-world applications, such as natural language processing (NLP), text mining, data cleaning, sentiment analysis, and customer feedback analysis.

**Examples:**
- Cleaning and preprocessing text data for an NLP model
- Extracting specific information from large text datasets
- Transforming unstructured text into structured data for analysis

## Loading and Inspecting Text Data

### Loading Text Data
Let's start by loading some text data into a Pandas DataFrame.

**Code Example: Loading Text Data**
```python
import pandas as pd

# Sample data
data = {
    'Name': ['Raj Kumar', 'Amit Sharma', 'Priya Singh', 'Sara Ali'],
    'Occupation': ['Data Scientist', 'Engineer', 'Doctor', 'Artist'],
    'Address': ['123 Elm St, Delhi', '456 Oak St, Mumbai', '789 Pine St, Bangalore', '101 Maple St, Pune']
}
data_frame = pd.DataFrame(data)
print("Original DataFrame:\n", data_frame)
```

## Cleaning Text Data

### Cleaning Text Data
Cleaning text data involves removing unwanted characters, correcting formatting, and standardizing text.

**Code Example: Cleaning Text Data**
```python
# Removing leading/trailing whitespace
data_frame['Name'] = data_frame['Name'].str.strip()

# Converting to lowercase
data_frame['Name'] = data_frame['Name'].str.lower()

# Removing special characters
data_frame['Address'] = data_frame['Address'].str.replace(r'\W', ' ', regex=True)

print("\nCleaned DataFrame:\n", data_frame)
```

## Extracting Information from Text Data

### Extracting Information
Extracting information involves pulling out specific parts of the text, such as extracting names, addresses, or other meaningful information.

**Code Example: Extracting Information**
```python
# Extracting first names
data_frame['First Name'] = data_frame['Name'].str.split().str[0]

# Extracting cities from addresses
data_frame['City'] = data_frame['Address'].str.extract(r'(\bDelhi\b|\bMumbai\b|\bBangalore\b|\bPune\b)')

print("\nDataFrame with Extracted Information:\n", data_frame)
```

## Manipulating Text Data

### Manipulating Text Data
Manipulating text data involves combining, splitting, and transforming text to suit your analysis needs.

**Code Example: Manipulating Text Data**
```python
# Combining columns
data_frame['Name_Address'] = data_frame['Name'] + ', ' + data_frame['Address']

# Splitting addresses into multiple columns
address_split = data_frame['Address'].str.split(',', expand=True)
data_frame['Street'] = address_split[0]
data_frame['City'] = address_split[1]

print("\nDataFrame with Manipulated Text Data:\n", data_frame)
```

## Applying Functions to Text Data

### Applying Functions
You can apply custom functions to text data for more complex transformations and analysis.

**Code Example: Applying Functions**
```python
# Custom function to count words in a string
def word_count(text):
    return len(text.split())

# Applying the custom function to the 'Occupation' column
data_frame['Occupation Word Count'] = data_frame['Occupation'].apply(word_count)

print("\nDataFrame with Word Count in Occupation:\n", data_frame)
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