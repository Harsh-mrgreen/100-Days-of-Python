from bs4 import BeautifulSoup


with open(file= "website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
# print(soup.title.string)
#print(soup.prettify())
#print(soup.a)
# to get all the particular type of tags --- findall()
all_anchor_tags = soup.find_all(name="a")
# if we wnated t get all the text of anchor tags --
#for tag in all_anchor_tags:
    #print(tag.getText())
    #to get all the links in a tags --
    #print(tag.get("href"))

# if we wanted to find something with a particular id ---
heading = soup.find(name="h1", id= "name")
#print(heading)

section_heading = soup.find(name = "h3", class_ = "heading")
#print(section_heading)

conpany_url = soup.select_one(selector="p a")
#print(conpany_url)


# we use # when selecting an id
name = soup.select_one(selector="#name")
#print(name)

# we use . when selecting a class

headings = soup.select(".heading")
print(headings)