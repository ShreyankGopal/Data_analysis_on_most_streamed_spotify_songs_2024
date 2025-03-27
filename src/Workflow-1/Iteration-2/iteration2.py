import pandas as pd
import seaborn as sns
import squarify
import matplotlib.pyplot as plt
import numpy as np
#pip install squarify
# Load the dataset
df = pd.read_csv('/content/most_streamed_spotify_songs_2024.csv')

# Display the first few rows
print(df.head())

# Calculate total streams for different platforms
Total_Tik_tok = df['TikTok Views'].sum()
print(Total_Tik_tok)

Total_Youtube = df['YouTube Views'].sum()
Total_Spotify = df['Spotify Streams'].sum()
Total_Pandora = df['Pandora Streams'].sum()
total_Soundcloud = df['Soundcloud Streams'].sum()

# Add a new column for total streams
df['Total Streams'] = df[['YouTube Views', 'Spotify Streams', 'TikTok Views']].sum(axis=1)

# Get the top 60 artists by total streams
top_60_artists = df.sort_values('Total Streams', ascending=False).head(60)

# Create a treemap for the top 60 artists
labels = [f"{artist}\n{streams}" for artist, streams in zip(top_60_artists['Artist'], top_60_artists['Total Streams'])]
plt.figure(figsize=(14, 8))
squarify.plot(
    sizes=top_60_artists['Total Streams'],
    label=labels,
    alpha=0.8,
    color=sns.color_palette("Blues", len(top_60_artists))
)
plt.title("Top 60 Artists by Total Streams (Treemap)", fontsize=16)
plt.axis('off')
plt.show()

# Create a treemap for the bottom half (last 30 of the top 60)
bottom_half = top_60_artists.tail(30)
labels = [f"{artist}\n{streams}" for artist, streams in zip(bottom_half['Artist'], bottom_half['Total Streams'])]
plt.figure(figsize=(14, 8))
squarify.plot(
    sizes=bottom_half['Total Streams'],
    label=labels,
    alpha=0.8,
    color=sns.color_palette("Blues", len(bottom_half))
)
plt.title("Zoomed in View", fontsize=16)
plt.axis('off')
plt.show()

# Pie chart analysis for batches of 20 artists
data = top_60_artists[['Artist', 'YouTube Views', 'Spotify Streams', 'TikTok Views']]
batch_size = 20

for i in range(0, len(data), batch_size):
    batch = data.iloc[i:i + batch_size]
    averages = batch[['YouTube Views', 'Spotify Streams', 'TikTok Views']].mean()

    plt.figure(figsize=(8, 8))
    plt.pie(
        averages,
        labels=averages.index,
        autopct='%1.1f%%',
        colors=['#ff9999', '#66b3ff', '#99ff99'],
        startangle=90
    )
    plt.title(f'Average Stream Distribution (Batch {i+1} to {i+batch_size})')
    plt.show()

# Bar plot analysis for batches of 20 artists
platforms = ['YouTube Views', 'Spotify Streams', 'TikTok Views']

for i in range(0, len(top_60_artists), batch_size):
    batch = top_60_artists.iloc[i:i + batch_size]
    artists = batch['Artist']
    data = batch[platforms].T

    x = np.arange(len(artists))
    bar_width = 0.15
    offset = 0

    plt.figure(figsize=(15, 8))
    for idx, platform in enumerate(platforms):
        plt.bar(x + offset, data.loc[platform], width=bar_width, label=platform)
        offset += bar_width

    for j in range(1, len(artists)):
        plt.axvline(j - 0.2, color='gray', linestyle='--', alpha=0.7)

    plt.xticks(x + bar_width * (len(platforms) / 2), artists, rotation=45, ha='right')
    plt.xlabel('Artists')
    plt.ylabel('Streams')
    plt.title(f'Stream Performance of Artists (Batch {i+1}-{i+batch_size})')
    plt.legend()
    plt.tight_layout()
    plt.show()
