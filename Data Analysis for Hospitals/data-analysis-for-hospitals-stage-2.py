import pandas as pd

pd.set_option('display.max_columns', 8)

general_df = pd.read_csv('test/general.csv')
prenatal_df = pd.read_csv('test/prenatal.csv')
sports_df = pd.read_csv('test/sports.csv')

prenatal_df.columns = general_df.columns
sports_df.columns = general_df.columns

df_concated = pd.concat([general_df, prenatal_df, sports_df], ignore_index=True)

df_concated.drop(columns=['Unnamed: 0'], inplace=True)

print(df_concated.sample(n=20, random_state=30))

"""
Stage 2/5: Merge them_
Description
Hooray, you have the datasets! However, they are somewhat difficult to work with.
They are divided into three parts, and the column names are different:
HOSPITAL and Sex in the prenatal, Hospital and Male/female in the sports facility.
We cannot study our data in full and perform statistical calculations.
It also stands in the way of good visualization.

In this stage, we will change the column names and merge our datasets into one.
To combine the columns, use the concat function and the ignore_index = True parameter.
After merging, a side Unnamed: 0 column will appear.
This column contains the indexes of the tables.
This column is not needed for the practical purposes of this project,
so we will delete it in this stage.

Objectives
The first two steps are the same as in the first stage.
The second stage requires completing the following steps:

After all the libraries imports write the following line of code:

pd.set_option('display.max_columns', 8)
Read 3 CSV files with datasets
Change the column names.
All column names in the sports and prenatal tables must match the column names in
the general table
Merge the data frames into one. Use the ignore_index = True parameter and
the following order: general, prenatal, sports
Delete the Unnamed: 0 column
Print random 20 rows of the resulting data frame.
For the reproducible output set random_state=30
"""