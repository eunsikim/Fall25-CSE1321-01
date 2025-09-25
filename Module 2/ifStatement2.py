def main():
    # Valid passwords must be 8 characters or longer
    # Valid passwords must be 16 characters or less
    # Valid passwords must contain special characters: !, #
    password = input("Enter your password: ")

    # password = helloWorld!#

    isValid = len(password) >= 8 and len(password) <= 16 and '!' in password and '#' in password
    # TRUE and TRUE and TRUE and TRUE
    # TRUE and TRUE and TRUE
    # TRUE and TRUE
    # TRUE          

    if isValid:
        print("Your password is valid")
    else:
        print("Passwords must be 8 to 16 characters and contain special characters (!, #)")

if __name__ == "__main__":
    main()