import pandas as pd

file_path = 'spotify_cleaned_1.csv'
df = pd.read_csv(file_path, encoding='ISO-8859-1')

df['Track Name Count'] = df.groupby('Track').cumcount() + 1

df['Track'] = df.apply(lambda x: f"{x['Track']} ({x['Track Name Count']})" if x['Track Name Count'] > 1 else x['Track'], axis=1)

df.drop('Track Name Count', axis=1, inplace=True)

print(df[['Track']].head())

df.to_csv('spotify_cleaned_3.csv',index=False)