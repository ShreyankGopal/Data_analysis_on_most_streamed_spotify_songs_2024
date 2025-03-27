import pandas as pd
import re
file_path = 'spotify_cleaned_1.csv'
df = pd.read_csv(file_path,encoding = 'ISO-8859-1')

df = df.drop(columns=['TIDAL Popularity','null_count','Release Date']).sort_index()

int("done")

df.to_csv('spotify_cleaned_1.csv',index=False)

df['null_count'] = df.isnull().sum(axis=1)
df_cleaned = df[df['null_count'] < 13]
df = df_cleaned.sort_values(by='null_count', ascending=False)