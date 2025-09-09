def main():
    USERNAME = "admin"
    PASSWORD = "password123"

    username_input = input("Username: ")
    password_input = input("Password: ")

    # Valid login
    # CHALLENGE: Print error message if BOTH username and password are incorrect!
    if USERNAME == username_input and PASSWORD == password_input:
        print("Succesful Login")
    elif USERNAME != username_input:
        print("Incorrect Username")
    elif PASSWORD != password_input:
        print("Incorrect Password")
    else:
        print("Invalid Credentials")

if __name__ == "__main__":
    main()