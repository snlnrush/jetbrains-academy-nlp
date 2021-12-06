import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

prenatal_df.columns = general_df.columns
sports_df.columns = general_df.columns

df_concated = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

df_concated.drop(columns=['Unnamed: 0'], inplace=True)

df_concated.dropna(axis=0, inplace=True, how='all')

df_concated['gender'].replace(['female', 'woman'], 'f', inplace=True)
df_concated['gender'].replace(['man', 'male'], 'm', inplace=True)
df_concated['gender'].replace(np.nan, 'f', inplace=True)

df_concated.replace(np.nan, 0, inplace=True)

df_concated.plot(y='age', kind='hist', bins=80)
plt.show()

df_concated['diagnosis'].value_counts().plot(kind='pie')
plt.show()

df_concated['age'].value_counts().plot(kind='box')
plt.show()

answer_1 = '15-35'
answer_2 = 'pregnancy'
answer_3 = 'fucking stage'

print(f'The answer to the 1st question: {answer_1}')
print(f'The answer to the 2nd question: {answer_2}')
print(f"The answer to the 3rd question: It's because {answer_3}")


"""
Description
Are you ready to catch sight of your data?

Graphics are arguably the most accessible way to represent the data and its structure. Sometimes, it can help to find the main data patterns and deviations. We will use data visualization methods to conclude our dataset.

In the last stage, you need to create data visualization to answer the following questions:

What is the most common age of a patient among all hospitals? Plot a histogram and choose one of the following age ranges: 0-15, 15-35, 35-55, 55-70, or 70-80
What is the most common diagnosis among patients in all hospitals? Create a pie chart
Build a violin plot of height distribution by hospitals. Try to answer the questions. What is the main reason for the gap in values? Why there are two peaks, which correspond to the relatively small and big values? No special form is required to answer this question
There is a comprehensive explanation of violin plots by Eryk Lewinson.
Hint

To answer the last question think about specializations of the hospitals in the dataset and the unit of measurement of height.
Please note that the answers are independent of each other.

At this stage, we recommend using pandas visualization tools. However, feel free to use seabornmatplotlib, or any other library.

The tests to check graph content are very limited and we are sure that you can easily answer the questions without plotting any charts. Despite this, please be curious to answer them using graphs. It is a very valuable skill for a data scientist to plot and interpret the data.
"""