import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

# REVISE THIS !!! - GO THROUGH THE DOCUMENTATION
CLIENT_ID = "e8e13a47a1ab43aabc61eca1eddb5461"
CLIENT_SECRET = "058ba35451ce436d86f28319c9d4ab6e"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("What year you would like to travel to in YYYY-MM-DD format: ")
URL = "https://www.billboard.com/charts/hot-100/" + date

response = requests.get(URL)

billboard_html = response.text
soup = BeautifulSoup(billboard_html, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist_data = sp.user_playlist_create(user=user_id, name=date+" Billboard 100", public=False)
playlist_id = playlist_data["id"]

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)


# --------------- RETURNS EVERYTHING APART FROM THE FIRST ITEM ------------------ #
# song_li = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex "
#                                           "lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 "
#                                           "u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 "
#                                           "lrv-u-padding-l-1@mobile-max")
#
#
# song_titles = [(song.find(name="h3", id="title-of-a-story").getText()).strip() for song in song_li]
#
# print(song_titles)
