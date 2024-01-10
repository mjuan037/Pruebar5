import pandas as pd
import json

# Cargar datos desde el archivo JSON
with open(r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\taylor_swift_spotify.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Crear un DataFrame con los datos de los artistas
df_artists = pd.json_normalize(data, sep='_')

# Crear un DataFrame con los datos de los álbumes
df_albums = pd.json_normalize(data, record_path='albums', sep='_', meta=['artist_id', 'artist_name', 'artist_popularity'])

# Crear un DataFrame con los datos de las pistas
df_tracks = pd.concat([pd.json_normalize(album, record_path='tracks', sep='_', meta=['album_id', 'album_name', 'album_release_date', 'album_total_tracks']) for album in data['albums']])

# Crear un DataFrame con los datos de las características de audio
df_audio_features = pd.concat([pd.json_normalize(track['audio_features']) for track in data['albums'][0]['tracks']])

# Combinar los DataFrames según sea necesario
# ...

# Guardar los DataFrames en archivos CSV si es necesario
df_artists.to_csv(r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\artistas.csv', index=False)
df_albums.to_csv(r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\albums.csv', index=False)
df_tracks.to_csv(r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\tracks.csv', index=False)
df_audio_features.to_csv(r'C:\Users\Chanchor\OneDrive - Universidad Piloto de Colombia\Documents\Prueba R5\audio_features.csv', index=False)
