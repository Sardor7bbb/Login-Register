import Login
import Register
def main():
    instagram = input("""
    1. Login
    2. Register
        >>> """)

    if instagram == "1":
        return Login.login()
    elif instagram == "2":
        return Register.register()
    else:
        print("Invalid")
        return main()

if __name__ == "__main__":
    main()
