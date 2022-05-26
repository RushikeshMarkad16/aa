# -*- coding: utf-8 -*-
"""Assignment_No_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iJqTz02PjrkXMIPbiE7owDI9AfzjIAJO

# Assignment No. 3

    Descriptive Statistics - Measures of Central Tendency and variability
    Perform the following operations on any open-source dataset (e.g., data.csv)
    
    1. Provide summary statistics (mean, median, minimum, maximum, standard deviation) for a dataset (age, 
        income etc.) with numeric variables grouped by one of the qualitative (categorical) variable. For example,
        if your categorical variable is age groups and quantitative variable is income, then provide summary 
        statistics of income grouped by the age groups. Create a list that contains a numeric value for each 
        response to the categorical variable.
    
    2. Write a Python program to display some basic statistical details like percentile, mean, standard deviation
        etc. of the species of 'Iris-setosa', 'Iris-versicolor' and 'Iris-viginica' of iris.csv dataset.

# Task-1
"""

# Commented out IPython magic to ensure Python compatibility.
#importing required libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#Loading dataset into pandas dataframe

df = pd.read_csv('covid_19_india.csv')

#Displays first 5 rows 

df.head()

#Displays last 5 rows

df.tail()

#Returns the number of null values in each column

df.isnull().sum()

#Used to get the initial statistics

df.describe()

#Returs a tuple conataining dimensios i.e no of rows and no of columns

df.shape

df.groupby('State/UnionTerritory').get_group('Maharashtra')

#To get Mean of cured and deaths grouped by state/UT.

df.groupby('State/UnionTerritory')[['Cured','Deaths']].mean()

#Max value group by State/UnionTerritory

df.groupby('State/UnionTerritory')[['Cured','Deaths']].max()

#Min value group by State/UnionTerritory
df.groupby('State/UnionTerritory')[['Cured','Deaths']].min()

#Standard Deviation group by State/UnionTerritory

df.groupby('State/UnionTerritory')[['Cured','Deaths']].std()

#Median value group by State/UnionTerritory

df.groupby('State/UnionTerritory')[['Cured','Deaths']].median()

#Initial Statistics group by State/UnionTerritory

df.groupby('State/UnionTerritory')['Cured'].describe()

"""# StudentPerformance"""

#Loading dataset into pandas dataframe

df2 = pd.read_csv('StudentsPerformance.csv')

#Displays first 5 rows
df2.head()

#Displays last 5 rows
df2.tail()

df2.isnull().sum()

#Mean value group by gender
df2.groupby('gender')[['math score','reading score','writing score']].mean()

#Max value group by gender
df2.groupby('gender')[['math score','reading score','writing score']].max()

#Min value group by gender
df2.groupby('gender')[['math score','reading score','writing score']].min()

#Standard Deviation group by gender
df2.groupby('gender')[['math score','reading score','writing score']].std()

#Median value group by gender
df2.groupby('gender')[['math score','reading score','writing score']].median()

#Quantile value group by gender
df2.groupby('gender')[['math score','reading score','writing score']].quantile()

#Mode value group by gender
df2.groupby('gender').agg(lambda x:x.value_counts().index[0])

"""# Task-2"""

#Loading dataset into pandas dataframe
df3=pd.read_csv('iris.csv')
df3

#Returs a tuple conataining dimensios i.e no of rows and no of columns
df3.shape

df3.isnull().sum()

#Used to get the initial statistics
def basic_stats(df):
    print("\n Iris-setosa")
    print(df[df.Species == 'Iris-setosa'].describe().transpose())
    print("\n Iris-versicolor")
    print(df[df.Species == 'Iris-versicolor'].describe().transpose())
    print("\n Iris-virginica")
    print(df[df.Species == 'Iris-virginica'].describe().transpose())

basic_stats(df3)

#Mean value group by Species
df3.groupby(df['Species'])[['SepalLengthCm','PetalLengthCm','SepalWidthCm','PetalWidthCm']].mean()

#Median value group by Species
df3.groupby(df['Species'])[['SepalLengthCm','PetalLengthCm','SepalWidthCm','PetalWidthCm']].median()

#Standard Deviation group by Species
df3.groupby(df['Species'])[['SepalLengthCm','PetalLengthCm','SepalWidthCm','PetalWidthCm']].std()

#Quantile value group by Species
df3.groupby(df['Species'])[['SepalLengthCm','PetalLengthCm','SepalWidthCm','PetalWidthCm']].quantile()

#Min value group by Species
df3.groupby(df['Species'])[['SepalLengthCm','PetalLengthCm','SepalWidthCm','PetalWidthCm']].min()

#Max value group by Species
df3.groupby(df['Species'])[['SepalLengthCm','PetalLengthCm','SepalWidthCm','PetalWidthCm']].max()

#Mode value group by Species
df3.groupby('Species').agg(lambda x:x.value_counts().index[0])

#Used to get initial statistics of all species
df3.groupby('Species')['SepalLengthCm'].describe()