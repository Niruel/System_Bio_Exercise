import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/List_of_virus_species'
page = requests.get(URL)
fileName = "mytxt.txt"
soup = BeautifulSoup(page.content, 'html.parser')
col = soup.findAll('title', class_='div-col columns column-width')
text = soup.get_text().strip()
print(text)
"""
file1 = open(fileName, 'w')
file1.writelines(text)
file1.close()
"""