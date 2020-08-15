from requests_html import HTMLSession

session =HTMLSession()
url="https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN:en"
r=session.get(url)
r.html.render()


data=r.find("#yDmH0d > c-wiz > div > div.FVeGwb.ARbOBb > div.BP0hze > div.xT64Qc > div > div.UnO7qd > div > div > div.fNm5wd.qs41qe > div.UvMayb",first=True)
print(data.text)
