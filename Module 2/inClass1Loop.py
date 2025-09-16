def main():
    USERNAME = "admin"
    PASSWORD = "password123"

    username_input = ""
    password_input = ""

    hasLoggedIn = False

    while USERNAME != username_input or PASSWORD != password_input:
        username_input = input("Username: ")
        password_input = input("Password: ")

        # Valid login
        if USERNAME == username_input and PASSWORD == password_input:
            print("Succesful Login")
            hasLoggedIn = True
        elif USERNAME != username_input and PASSWORD != password_input:
            print("Incorrect Username and incorrect Password")
        elif USERNAME != username_input:
            print("Incorrect Username")
        elif PASSWORD != password_input:
            print("Incorrect Password")
        else:
            print("Invalid Credentials")
        
        if not hasLoggedIn:
            print("Try again\n")

if __name__ == "__main__":
    main()