from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies = [movie.getText() for movie in all_movies]
movies.reverse()

with open("movies", "w") as file:
    for num in movies:
        file.write(f"{num}\n")






