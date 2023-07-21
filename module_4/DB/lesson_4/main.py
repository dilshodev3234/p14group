from dataclasses import dataclass
import psycopg2

class DB:
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password=1,
        host='localhost',
        port=5432
    )

    cur = con.cursor()
    def insert(self):
        table_name = self.__class__.__name__.lower()
        fields = ' , '.join(self.kwargs.keys())
        soroq = ' , '.join(["%s"]*len(self.kwargs.keys()))


        params = tuple(self.kwargs.values())
        query = f"""insert into {table_name} ({fields}) values ({soroq})"""
        self.cur.execute(query , params)
        self.con.commit()


class Users(DB):
    def __init__(self , **kwargs):
        self.kwargs = kwargs

class Products(DB):
    def __init__(self , **kwargs):
        self.kwargs = kwargs

# Users(first_name = "Botirjon" , last_name = "Botirov" , email = "Botirjon@gmail.com").insert()
Products(product_name = "Tesla" , price = 1000).insert()