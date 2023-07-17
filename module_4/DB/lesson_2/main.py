# pip install psycopg2-binary
import psycopg2

a = 2








con = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password=1,
    host='localhost',
    port=5432
)

cur = con.cursor()

def rename_column(table_name:str , old_col_name: str, new_col_name:str) -> None:
    query = f"""
        alter table if exists {table_name} rename column {old_col_name} to {new_col_name};
    """
    try:
        cur.execute(query)
        con.commit()
    except :
        print("xatolik")


users_create = """
    create table if not exists users(
        id serial primary key,
        fullname varchar(255) not null
    );
"""
# cur.execute(users_create)
# rename_column("users" , "fullname","name")

table_list = """
SELECT users
  FROM information_schema.tables
 WHERE table_schema='public'"""


column_name = """
SELECT
    column_name
FROM
    information_schema.columns
WHERE
    table_name = 'users';"""
cur.execute(query)
print(cur.fetchall())
