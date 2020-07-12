"""This script is used to track the total case in india."""
import requests
from bs4 import BeautifulSoup
import time
url="https://ncov2019.live/"
q=requests.get(url)
soup=BeautifulSoup(q.text,"lxml")
print(soup.find_all("td",class_="text--green text--green"))
for j in soup.find_all("td"):
	print((j.text))
	break
