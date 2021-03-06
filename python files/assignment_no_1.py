# -*- coding: utf-8 -*-
"""Assignment_No_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pKyta29ndx0yPvVAbqi6hc1ZklQtlwnP
"""

Perform the following operations using Python on any open-source dataset (e.g., data.csv)
1.	Import all the required Python Libraries.
2.	Locate an open-source data from the web (e.g. https://www.kaggle.com). Provide a clear description of the data and its source (i.e., URL of the web site).
3.	Load the Dataset into pandas’ data frame.
4.	Data Preprocessing: check for missing values in the data using pandas isna (), describe() function to get some initial statistics. Provide variable descriptions. Types of variables etc. Check the dimensions of the data frame.
5.	Data Formatting and Data Normalization: Summarize the types of variables by checking the data types (i.e., character, numeric, integer, factor, and logical) of the variables in the data set. If variables are not in the correct data type, apply proper type conversions.
6.	Turn categorical variables into quantitative variables in Python.
In addition to the codes and outputs, explain every operation that you do in the above steps and explain everything that you do to import/read/scrape the data set.

import pandas as pd
import numpy as np
# pd.options.mode.chained_assignment = None

# https://www.kaggle.com/uciml/iris

df = pd.read_csv('Iris.csv')
df

pd.isna(df)

df.describe()

df.dtypes

df.shape

# dealing with missing values
df.isna().sum()

df = df.dropna(axis = 0)
df

df.shape

df.isna().sum()

# Normalization

df['SepalLengthCm'] = df['SepalLengthCm']/df['SepalLengthCm'].max()
df['PetalLengthCm'] = df['PetalLengthCm']/df['PetalLengthCm'].max()
df['SepalWidthCm'] = df['SepalWidthCm']/df['SepalWidthCm'].max()
df['PetalWidthCm'] = df['PetalWidthCm']/df['PetalWidthCm'].max()
df

df['Species'].replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],[0, 1, 2], inplace = True)
df