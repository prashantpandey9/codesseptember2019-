import json
import bs4
import requests

def crawl():
    url="https://www.imdb.com/chart/top/?sort=rk,asc&mode=simple&page=1" #URL for movies
    e=requests.get(url)
    q=BeautifulSoup(e.text,'html')
    p1=q.find_all("td",class_="titleColumn")
    p2=q.find_all("span",class_="secondaryInfo")
    p3 =q.find_all('td',class_="ratingColumn imdbRating")
    movie=[j.text  for n in p1 for j in n.find_all('a')]
    year=[v.text.strip() for v in p2]
    rating=[i.text.strip() for i in p3]
    serial=1
    dic={}
    for j in range(len(movie)):
        dic[serial]={"Movie_name":movie[j],"Release_year":year[0],"IMDb_Rating":rating[0]}
        serial+=1

    with open('IMDB.txt', 'w') as json_file:
       json.dump(dic, json_file)


crawl() # function call
