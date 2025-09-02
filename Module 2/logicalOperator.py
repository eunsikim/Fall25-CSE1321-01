def main():
    # Valid passwords must be 8 characters or longer
    # Valid passwords must be 16 characters or less
    # Valid passwords must contain special characters: !, #
    password = input("Enter your password: ")

    # isValid = len(password) >= 8
    # isValid = '!' in password or '#' # Why is this happening
    # isValid = len(password) >= 8 and len(password) <= 16

    isValid = len(password) >= 8 and len(password) <= 16 and '!' in password and '#' in password

    print(isValid)

if __name__ == "__main__":
    main()