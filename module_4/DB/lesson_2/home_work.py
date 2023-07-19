import psycopg2



class Table:
    con = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password=1,
        host='localhost',
        port=5432
    )

    cur = con.cursor()

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def select_tables(self):
        query = """
            SELECT table_name 
            FROM information_schema.tables
            WHERE table_schema='public'
        """
        self.cur.execute(query)
        for i, table_name in enumerate(self.cur.fetchall()):
            print(f"{i}) {table_name[0]}")

    def create_table(self):
        columns = []
        for k , v in self.kwargs.items():
            if k != "table_name":
                columns.append(f"{k} {v}")
        columns = " , ".join(columns)


        query = f"""
            create table if not exists {self.kwargs.get('table_name')}(
                {columns}
            );
        """
        self.cur.execute(query)
        self.con.commit()


    def table_column(self):
        query = f"""
            SELECT
            column_name
        FROM
            information_schema.columns
        WHERE
            table_name = '{self.kwargs.get('table_name')}';
        """
        self.cur.execute(query)
        return self.cur.fetchall()

    def rename_column(self):
        table_name = self.kwargs.get("table_name")
        old_name = self.kwargs.get("old_col")
        new_name = self.kwargs.get("new_col")
        query = f"""
            alter table {table_name} rename column {old_name} to {new_name};
        """
        self.cur.execute(query)
        self.con.commit()


data_types = ["serial primary key", "varchar", "text", "integer", "bool"]


def show_data_type():
    for i, data_type in enumerate(data_types, 1):
        print(f"{i}) {data_type}")


def UI():
    text = """
        1) create table 
        2) drop table
        3) show table
        4) rename column
        5) truncate table
        >>>"""
    key = int(input(text))
    match key:
        case 1:
            Table().select_tables()
            table_name = input("Table name:")
            fields = dict()
            continue_ = True
            while continue_:
                column_name = input("Column name")
                show_data_type()
                data_type = data_types[int(input(">>>")) - 1]
                if data_type == "varchar":
                    max_l = input("Max length : ")
                    data_type = f"varchar({max_l})"
                fields[column_name] = data_type
                is_con = input("continue [Yes/no]>>>")
                if is_con == "no":
                    continue_ = False
            Table(**fields , table_name = table_name).create_table()
            print("Successfully created table")

        case 2:
            pass
        case 3:
            pass

        case 4:
            Table().select_tables()
            table_name = input("Table name : ")
            columns = Table(table_name = table_name).table_column()
            for i , col in enumerate(columns, 1):
                print(f"{i}) {col[0]}")
            old_col = columns[int(input(">>>"))-1][0]
            new_col = input("New Column:")
            Table(table_name=table_name , old_col=old_col, new_col=new_col).rename_column()
            print("Success rename column !")

        case 5:
            pass


UI()
