
from database_db import Database

def create():

    users = """
    CREATE TABLE IF NOT EXISTS users (
    users_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    username VARCHAR(20),
    email VARCHAR(50),
    phon_number VARCHAR(9),
    password VARCHAR(4))
    """
    print(f"{users} => created{Database.connect(users, "create")}")

if __name__ == "__main__":
    create()
