import pandas as pd
df_tracks=pd.read_csv('SpotifyFeatures.csv')
df_users=pd.read_excel('Spotify_data.xlsx')
df_users.columns=df_users.columns.str.strip()
df_tracks.columns=df_tracks.columns.str.strip()
df_tracks=df_tracks.dropna(subset=['track_name'])
df_users['preffered_premium_plan']=df_users['preffered_premium_plan'].fillna('no plan selected')
pod_columns=['fav_pod_genre','preffered_pod_format','pod_host_preference', 'preffered_pod_duration']
for col in pod_columns:
    df_users[col] = df_users[col].fillna('Non-Podcast Listener')
genre_map = {
    'classical': 'Classical',
    'Classical & melody, dance': 'Classical',
    'Electronic/Dance': 'Electronic',
    'Rap': 'Rap',
    'Pop': 'Pop',
    'Rock': 'Rock',
    'Melody': 'Acoustic',
    'Old songs': 'Folk',
    'Kpop': 'Pop',
    'All': 'Pop', 
    'trending songs random': 'Pop'
}

df_users['fav_music_genre_clean'] = df_users['fav_music_genre'].map(genre_map).fillna('Pop')
def classify_user(row):
    plan = str(row['spotify_subscription_plan'])
    willingness = str(row['premium_sub_willingness'])
    
    if 'Free' in plan:
        return 'High Potential Free' if willingness == 'Yes' else 'Standard Free'
    return 'Existing Premium'

df_users['user_conversion_segment'] = df_users.apply(classify_user, axis=1)
genre_summary = df_tracks.groupby('genre').agg({
    'danceability': 'mean',
    'energy': 'mean',
    'valence': 'mean',
    'popularity': 'mean',
    'loudness': 'mean',
    'tempo': 'mean',
    'track_id': 'count'
}).reset_index().rename(columns={'track_id': 'total_tracks'})
df_users.to_csv('cleaned_spotify_users.csv', index=False)
df_tracks.to_csv('cleaned_spotify_tracks.csv', index=False)
genre_summary.to_csv('spotify_genre_audio_summary.csv', index=False)

print(" Bütün təmizlənmə və hazırlanma bitdi")
