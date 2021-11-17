import numpy as np
import pandas as pd

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

print('Data shape:', df_concated.shape)
print(df_concated.sample(n=20, random_state=30))


"""
Stage 3/5: Improve your dataset
Description
Some cells in our table have NaN as values: the patient gender is not defined in the prenatal hospital, and the test columns are empty in all three tables. We still cannot commit to the analysis as the statistics are not going to be objective. We have to correct the table for further study.

Let's take a closer look at the gender column. It's a big mess: there we have female, male, man, woman. You need to correct the data in this column. The values should be either f or m. Replace the empty gender column values for prenatal patients with f (we can assume that the prenatal treats only women).

The bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns also need to be corrected. Replace the NaN values of the columns above with zeros.

Objectives
Steps 1-5 are the same as in the previous stage. The third stage requires completing the following steps:

After all the libraries imports write the following line of code:
pd.set_option('display.max_columns', 8)
Read the CSV files with datasets
Change the column names. The column names of the sports and the prenatal tables must match the column names of the general table

Merge the data frames into one. Use the ignore_index = True parameter and the following order: general, prenatal, sports
Delete the Unnamed: 0 column
Delete all the empty rows
Correct all the gender column values to f and m respectively
Replace the NaN values in the gender column of the prenatal hospital with f
Replace the NaN values in the bmi, diagnosis, blood_test, ecg, ultrasound, mri, xray, children, months columns with zeros
Print shape of the resulting data frame
Print random 20 rows of the resulting data frame. For the reproducible output set random_state=30
"""