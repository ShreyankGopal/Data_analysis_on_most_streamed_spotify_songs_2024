import pandas as pd
import re
file_path = 'spotify_cleaned_1.csv'
df = pd.read_csv(file_path,encoding = 'ISO-8859-1')

def my_function(word):
    return word.replace(",","")

df[['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'YouTube Views', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach']] = df[['Spotify Streams', 'Spotify Playlist Count', 'Spotify Playlist Reach', 'YouTube Views', 'YouTube Likes', 'TikTok Posts', 'TikTok Likes', 'TikTok Views', 'YouTube Playlist Reach']].astype(str).applymap(my_function)
df[['AirPlay Spins','Deezer Playlist Reach', 'Pandora Streams',	'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']] = df[['AirPlay Spins','Deezer Playlist Reach', 'Pandora Streams',	'Pandora Track Stations', 'Soundcloud Streams', 'Shazam Counts']].astype(str).applymap(my_function)

unwanted_chars = r'[ýý|¿½|ï]'

def is_dd_mm_yyyy(date_str):
    pattern = r'\d{2}-\d{2}-\d{4}'
    return bool(re.match(pattern, date_str))

df['Release Date'] = df['Release Date'].apply(lambda x: x if is_dd_mm_yyyy(x) else pd.to_datetime(x, dayfirst=False, errors='coerce').strftime('%d-%m-%Y'))

df = df[~df.apply(lambda row: row.astype(str).str.contains(unwanted_chars, regex=True).any(), axis=1)]

df_sorted = df.sort_index()

df_sorted.to_csv('spotify_cleaned.csv', index=False)