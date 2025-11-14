import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from pprint import pprint

client_id = '3c9d7c27a8fc4870ad2ee601957018e7'
client_secret = '92b5af97fffc47b9821989244352c48e'

client_credentials_manager = SpotifyClientCredentials(client_id= client_id, client_secret= client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# API에서 데이터를 가져오는 코드
artist_name = []
track_name = []
track_popularity = []
artist_id = []
track_id = []
track_images = []

for i in range(0, 1000, 50):
    track_results = sp.search(q='year:2021', type='track', limit=50, offset=i)
    
    # JSON 데이터로 저장
    with open('track_results.json', 'a') as json_file:
        json.dump(track_results, json_file)
        json_file.write("\n")  # 각 결과를 줄바꿈으로 구분하여 저장