import random

import Login
from database_db import Database
import random

def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number: +998 ")
    run = random.randint(999, 10000)
    print(f"SMS xabar: {run}")
    sms = input("SMS xabarni kiritning: ")
    while int(sms) != int(run):
        print(f"SMS xabar notog'ri qaytadan kiriting: ")
        run = random.randint(999, 10000)
        print(f"SMS xabar: {run}")
        sms = input("SMS xabarni kiritning: ")

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    password2 = input("Repeat password: ")
    while password != password2:
        print("Password mos kelmadi qaytadan kiriting:")
        password = input("Enter your password: ")
        password2 = input("Repeat password: ")

    query = f"INSERT INTO users (first_name, last_name, username, email, phon_number, password) VALUES ('{first_name}', '{last_name}', '{username}', '{email}','{phone_number}','{password}')"
    Database.connect(query, "insert")
    print("Xizmat muvofaqiyatli yakunlandi")
    return Login.login()
