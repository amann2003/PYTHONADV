from bs4 import BeautifulSoup
file=open("index.html")
contents=file.read()
file.close()

soup=BeautifulSoup(contents,"html.parser")
#html parser detects html file
#print(soup.title)
#print(soup.a)
#print(soup.h1)
"""print(soup.find_all(name= "a"))
all_links=soup.find_all(name="a")
for link in all_links:
    print(link.getText())

first_heading=soup.find(name="h1",id="first-heading")
print(first-heading.getText())
#.get(href) to access attributes

first_heading=soup.select(selector="div.links")
print(first_heading)
"""
response=requests.get(" https://news.ycombinator.com/")
contents=response.text
soup=BeautifulSoup(contents,"html.parser")
print(soup)