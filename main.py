import requests
from bs4 import BeautifulSoup

#Get url from user
url = "https://codewithharry.com"

#Get HTML file of that url

r = requests.get(url)
contents = r.content


#Parsing the HTML contents

soup = BeautifulSoup(contents, "html.parser")

#Get title of that webpage
Title = soup.title
"print(Title)"


#Get all Paragraphs of that webpage

paras = soup.find_all("p")
#print(paras)

tagss = soup.find_all("a")
#print(tagss)

#Get class
print(soup.find("p")["class"])


#Find all elements with class lead
print(soup.find_all("p",class_= "lead"))

#Extract text from tags/soup
print(soup.find("p").get_text())

#Extract text from tags/soup (Whole site)
print(soup.get_text())

anchors = soup.find_all("a")
links = set()

for link in anchors:
    if link.get("href") != "#":
        new_link = "https://codewithharry.com/"+link.get("href")
        links.add(new_link)

for i in links:
    print(i)

