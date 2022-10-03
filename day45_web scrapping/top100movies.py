from bs4 import BeautifulSoup
import requests

response = requests.get(url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup= BeautifulSoup(data, "html.parser")

movies_list = soup.find_all(name = "h3", class_= "title")[::-1]
movies = []
for movie in movies_list:
    each_movie = movie.getText()
    movies.append(each_movie)

    
with open(file ="movies.txt",mode="w") as file:
    for movie in movies_list:
        each_movie = movie.getText()
        file.write(f"{each_movie}\n")