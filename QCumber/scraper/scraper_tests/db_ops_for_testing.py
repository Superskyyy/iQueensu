"""
This module is for spider => PostgreSQL operations
"""
import datetime
import json

# this is just for some fun dont use this class.
#import psycopg2

from QCumber.scraper.assets.settings import SCRAPER_DB_CREDENTIALS as DB


class DatabaseOps:
    # single thread method

    def __init__(self):
        self.conn = psycopg2.connect(database=DB["database"],
                                     user=DB["username"], password=DB["password"], host=DB["host"], port=DB["port"])
        self.cursor = self.conn.cursor()

    def pg_batch_insert(self, table_name, course_data):
        pass

    def pg_insert(self, table_name, course_data):

        current_time = datetime.datetime.today().strftime('%Y-%m-%d')

        self.cursor.execute(
            f"INSERT INTO {table_name} (scrape_date, course_info) VALUES (%s,%s)",(current_time,json.dumps(course_data)))
        self.conn.commit()
       # {json.dumps(course_data)}

    def pg_delete(self):
        pass

    def pg_table_create(self, sql_stmt):

        try:
            self.cursor.execute(sql_stmt)
        except Exception:
            print("Table Creation failed.")

        print("Table created successfully")

        self.conn.commit()

    def pg_table_drop(self, table_name):

        self.cursor.execute('''DROP TABLE IF EXISTS ''' + table_name + '''CASCADE;''')
        self.conn.commit()


if __name__ == '__main__':
    my_conn = DatabaseOps()

    # table creation test
    my_conn.pg_table_create('''CREATE TABLE COURSE_CATALOG (
         ID SERIAL NOT NULL PRIMARY KEY,
         scrape_date DATE NOT NULL DEFAULT CURRENT_DATE, 
         course_info JSONB NOT NULL
         );''')

    # table deletion test
    my_conn.pg_table_drop(table_name="abc")

    # data insertion test

    json_example0 = [1, [2, 3], {'a': [4, 5]}]
    json_example1 = {
        "course_name": "INTRODUCTION TO DEBUGGING",
        "course_id": "330",
        "course_description": "I don\'t even know"
        }
    my_conn.pg_insert("COURSE_CATALOG", json_example1)

    # Always close connection after querying
    my_conn.conn.close()
