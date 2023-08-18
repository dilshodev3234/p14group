from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup


def news_data():
    start = time.time()
    response = requests.get("https://daryo.uz/yangiliklar")

    html = response.content.decode()

    soup = BeautifulSoup(html , "html.parser")

    datas = []
    for i in soup.find_all("div", {"class": "mini__article"})[:4]:
        data = {"title" : i.h3.text,
        "photo_link" : i.find("a", {"class": "border mini__article-img"}).img["data-src"],
        "date" : f"{datetime.today().date()}, {i.time.text.split(',')[-1]}"}
        datas.append(data)
    print(time.time() - start)
    return datas





