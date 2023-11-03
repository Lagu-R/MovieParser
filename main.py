# import modules
from bs4 import BeautifulSoup
import requests


# WebSite link 
WEB_ENDPOINT = "https://www.empireonline.com/movies/features/best-movies-2/"
# respone variable for our request's 


response = requests.get(WEB_ENDPOINT)
target_web = response.text


# start parse here
soup = BeautifulSoup(target_web , "html.parser")


# get all movie title from HTML h3 tag & class which are same for all title
nameOfMovies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")


# list comprehension to get only movie TiTle 
# instead of 
# (<h3 class="listicleItem_listicle-item__title__hW_Kn">100) Reservoir Dogs</h3>)
movies = [movie.getText() for movie in nameOfMovies]


# reverse numeration of movies .
movie_list = movies[::-1]


# rewrite or create file to adding data in.
with open("movie.text", mode="w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")


## ## also second edition ## ##
# for movie in nameOfMovies:
#     name = movie.get_text()
#     with open("movie.txt", "a") as data:
#         data.write(f"{str(name)}\n")
