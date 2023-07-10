import sqlite3
import time
from multiprocessing import Pool

import httpx

request_list = ["posts" , "comments", "albums" , "users" , "photos"]

con = sqlite3.connect("request_thread.sqlite")
cur = con.cursor()
users_table = """
    create table if not exists users (
        id integer primary key,
        name varchar(255),
        username varchar(255),
        email varchar(255),
        phone varchar(255),
        website varchar(255)
    );
"""
comments_query = """
        CREATE TABLE IF NOT EXISTS comments(
        postId INTEGER NOT NULL,
        id INTEGER PRIMARY KEY ,
        name VARCHAR(255),
        email VARCHAR(255),
        body TEXT
        );
    """

photos_table = """
    create table if not exists photos(
    albumId integer ,
    id integer primary key,
    title varchar (255),
    url varchar (255),
    thumbnailurl varchar (255)
        );
    """

posts_table = """
    create table if not exists posts(
        userId integer, 
        id integer primary key,
        title varchar(255),
        body text 
    );
"""

albums_table = """
    create table if not exists albums (
    userId integer,
    id integer primary key,
    title varchar(100)
    );
"""
cur.execute(posts_table)
cur.execute(albums_table)
cur.execute(comments_query)
cur.execute(users_table)
cur.execute(photos_table)
con.commit()


def save_data(table_name):
    response = httpx.get(f"https://jsonplaceholder.typicode.com/{table_name}")
    data = response.json()
    if not table_name == "users":
        fields = " , ".join(data[0].keys())
        soroq = " , ".join(['?']*len(data[0]))
        query = f"""insert into {table_name} ({fields}) values ({soroq})"""
        for i in data:
            cur.execute(query , tuple(i.values()))
            con.commit()
    else:
        d = data[0].copy()
        del d["company"]
        del d["address"]

        fields = " , ".join(d.keys())
        soroq = " , ".join(['?'] * len(d))
        query = f"""insert into {table_name} ({fields}) values ({soroq})"""
        for i in data:
            del i["company"]
            del i["address"]
            cur.execute(query, tuple(i.values()))
            con.commit()


start = time.time()
with Pool() as pool:
    pool.map(save_data , request_list)
print(time.time() - start)



