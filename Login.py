
from database_db import Database
import main
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    query = """SELECT * FROM users"""
    data = Database.connect(query, "select")
    for i in data:
        if username == i[3] and password == i[6]:
            print(f""" Salom {i[1]} {i[2]} xush kelibsiz (^_^) """)
            return main.main()
    print("Malumot topilmadi qaytadan urinib ko'ring")
    return login()
