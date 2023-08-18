import requests
from bs4 import BeautifulSoup

response = requests.get("https://kundalik.com/")

html = response.content.decode()

soup = BeautifulSoup(html , "html.parser")
# print(soup.prettify())


# for i in soup.find_all("div", {"class":"slider__icons__item__label"}):
#     print(i.text)

for i in soup("li" , {"class":"menu__layout_unit"}):
    with open(f"{i.a['href'].split('/')[-1]}.txt",'w') as f:
        f.write(requests.get(i.a['href']).content.decode())

