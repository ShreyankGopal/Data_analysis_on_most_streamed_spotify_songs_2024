import pandas as pd

# Load the dataset
df = pd.read_csv('merged.csv')
print(df.head())
print(df.shape)

# Define the columns related to views
views_columns = ['Spotify Streams', 'TikTok Views', 'YouTube Views']

# Function to classify songs based on view percentages
def classify_song(row, views_columns):
    total_views = row[views_columns].sum()

    if total_views == 0:
        return 'Even'  # Handle edge case where no views exist

    spotify_percentage = (row['Spotify Streams'] / total_views) * 100
    tiktok_percentage = (row['TikTok Views'] / total_views) * 100
    youtube_percentage = (row['YouTube Views'] / total_views) * 100

    if spotify_percentage > youtube_percentage and spotify_percentage > tiktok_percentage:
        return 1  # Spotify is dominant
    elif youtube_percentage > spotify_percentage and youtube_percentage > tiktok_percentage:
        return 2  # YouTube is dominant
    elif tiktok_percentage > spotify_percentage and tiktok_percentage > youtube_percentage:
        return 3  # TikTok is dominant
    else:
        return 0  # Tie or no clear dominance

# Apply the classification function to the DataFrame
df['category'] = df.apply(classify_song, axis=1, views_columns=views_columns)

# Get the minimum energy value
e_min = df['energy'].min()
print("Minimum energy value:", e_min)

# Filter top 10 unique artists for each category
spotify_dom = df[df['category'] == 1].drop_duplicates(subset='artists').head(10)
youtube_dom = df[df['category'] == 2].drop_duplicates(subset='artists').head(10)
tiktok_dom = df[df['category'] == 3].drop_duplicates(subset='artists').head(10)
no_dom = df[df['category'] == 0].drop_duplicates(subset='artists').head(10)

# Check the shape of Spotify dominant DataFrame
print("Spotify dominant shape:", spotify_dom.shape)

# Convert explicit column to integers for all categories
spotify_dom['explicit'] = spotify_dom['explicit'].astype(int)
youtube_dom['explicit'] = youtube_dom['explicit'].astype(int)
tiktok_dom['explicit'] = tiktok_dom['explicit'].astype(int)
no_dom['explicit'] = no_dom['explicit'].astype(int)

# Save the results to CSV files
spotify_dom.to_csv('spotify_dom.csv', index=False)
youtube_dom.to_csv('youtube_dom.csv', index=False)
tiktok_dom.to_csv('tiktok_dom.csv', index=False)
no_dom.to_csv('no_dom.csv', index=False)

# Describe statistics for Spotify dominant songs
spotify_stats = spotify_dom[['liveness', 'valence', 'tempo']].describe()
print(spotify_stats)
