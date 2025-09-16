def main():
    USERNAME = "admin"
    PASSWORD = "password123"

    hasLoggedIn = False

    counter = 0

    while True:
        username_input = input("Username: ")
        password_input = input("Password: ")

        # Valid login
        if USERNAME == username_input and PASSWORD == password_input:
            print("Succesful Login")
            hasLoggedIn = True
            break
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
        
        counter += 1

        if counter == 3:
            print("You've reached the maximum amount of tries")
            break
        else:
            print(f"This is try #{counter}, you have {3 - counter} tries left")
    
    if hasLoggedIn:
        print("User has succesfully logged in")

if __name__ == "__main__":
    main()