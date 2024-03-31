
import psycopg2 as db
import os
from dotenv import load_dotenv
load_dotenv()

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database=os.getenv("DATABASE_NAME"),
            host=os.getenv("DATABASE_HOST"),
            user=os.getenv("DATABASE_USER"),
            password=os.getenv("DATABASE_PASSWORD")

        )
        cursor = database.cursor()
        cursor.execute(query)

        if query_type == "select":
            return cursor.fetchall()
        else:
            return database.commit()