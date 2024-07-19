from bs4 import BeautifulSoup
import requests
import spotipy
import spotipy.oauth2 

BILLBOARD_TOP_100_WEBSITE = "https://www.billboard.com/charts/hot-100/2000-08-12"
USERNAME = '31evlwc5wpqo4dlujfhkj6r7to34'
CLIENT_ID = '877718e4f81a49f4ae40f95ffe21430d'
CLIENT_SECRET = 'e3901d5b70754061a2f898faaeef27ee'
SPOTIFY_DISPLAY_NAME = "Trilochan Yannawar"

# ------------------------------------------ Scraping top 100 songs ------------------------------------------
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/"+date)
content = response.text
soup = BeautifulSoup(content, "html.parser")
headings = soup.select("li ul li h3")

song_names = [heading.get_text().strip() for heading in headings]
# print(song_names)
# --------------------------------------- Authenticating with spotify ---------------------------------------

sp = spotipy.Spotify(
    auth_manager=spotipy.oauth2.SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


