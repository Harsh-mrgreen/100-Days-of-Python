from bs4 import BeautifulSoup
import requests
import soupsieve

response = requests.get(url = "https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

a_tags = soup.find_all(name = "a", class_ = "titlelink")
scores = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_ = "score")]

# for index in range(len(a_tags)):
#     print(a_tags[index].getText())
#     print(a_tags[index].get("href"))
article_texts = []
article_links = []

for tag in a_tags:
    text = tag.getText()
    article_texts.append(text)
    link = tag.get("href")
    article_links.append(link)

    
# print(len(article_texts))   
# print(article_links)
# print(len(scores))

highest = max(scores)
index = scores.index(highest)
print(highest)
print(article_links[index])
print(article_texts[index])