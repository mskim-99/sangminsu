# pip install spotipy
# 이때 주의할 점은 module명이 spotify가 아닌 spotipy이다!

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint


cid = '3c9d7c27a8fc4870ad2ee601957018e7'
secret = '92b5af97fffc47b9821989244352c48e'
redirect_uri = 'https://localhost:8000/callback'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid, client_secret=secret, redirect_uri=redirect_uri))

result = sp.search('iu',limit=2,type = 'artist')
pprint.pprint(result)