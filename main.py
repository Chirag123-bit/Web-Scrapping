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
print(Title)


#Get all Paragraphs of that webpage

paras = soup.find_all("p")
#print(paras)

tagss = soup.find_all("a")
print(tagss)

