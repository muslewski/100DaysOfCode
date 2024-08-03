from os import environ
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests

CLIENT_ID = environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = environ.get("SPOTIFY_CLIENT_SECRET")
CLIENT_URI = "http://example.com"
SCOPE = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=CLIENT_URI, scope=SCOPE, show_dialog=True, cache_path="token.txt"))

user = sp.current_user()
user_id = user["id"]


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

top100div = soup.find_all(class_="o-chart-results-list-row-container")

top100titles = [div.find(class_="c-title").get_text().strip() for div in top100div]

songs_uris = []
year = date.split("-")[0]

print(top100titles)

for song in top100titles:
    try:
        results = sp.search(q=f"track:{song} year:{year}", type="track")
        song_uri = results["tracks"]["items"][0]["uri"]
        songs_uris.append(song_uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=songs_uris)