import requests
from bs4 import BeautifulSoup
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_archive_html = response.text
soup = BeautifulSoup(empire_archive_html, "html.parser")

movie_names = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movie_names.reverse()
print(movie_names)

with open("movies.txt", mode="w") as text_file:
    for movie in movie_names:
        text_file.write(f"{movie} \n")
