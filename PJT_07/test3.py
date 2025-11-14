import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from pprint import pprint

client_id = '3c9d7c27a8fc4870ad2ee601957018e7'
client_secret = '92b5af97fffc47b9821989244352c48e'

client_credentials_manager = SpotifyClientCredentials(client_id= client_id, client_secret= client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# JSON 형식의 API를 반복을 통해 리스트에 담고, 각 리스트에 담긴 데이터를 PANDAS로 데이터프레임으로 만드는 과정입니다.

artist_name =[]
track_name = []
track_popularity =[]
artist_id =[]
track_id =[]
track_images = []
for i in range(0,1000,50):
    track_results = sp.search(q='year:2021', type='track', limit=50, offset=i)
    for i, t in enumerate(track_results['tracks']['items']):
        artist_name.append(t['artists'][0]['name'])
        artist_id.append(t['artists'][0]['id'])
        track_name.append(t['name'])
        track_id.append(t['id'])
        track_popularity.append(t['popularity'])
        track_images.append(t['album']['images'][0]['url'])
        
track_df = pd.DataFrame({'track_name' : track_name, 'track_id' : track_id, 'track_popularity' : track_popularity, 'artist_name' : artist_name, 'artist_id' : artist_id, 'track_image_link': track_images})
pprint(track_df)