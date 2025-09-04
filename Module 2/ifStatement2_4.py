def main():
    # Valid passwords must be 8 characters or longer
    # Valid passwords must be 16 characters or less
    # Valid passwords must contain special characters: !, #
    # ADD A NEW RULE: Valid passwords must contain a number
    password = input("Enter your password: ")

    isValidLen = len(password) >= 8 and len(password) <= 16
    hasSpecChar = '!' in password and '#' in password
    hasNumber = '1' in password or '2' in password or '3' in password or '4' in password or '5' in password or '6' in password or '7' in password or '8' in password or '9' in password or '0' in password

    isValid = isValidLen and hasSpecChar and hasNumber

    if isValid:
        print("Your password is valid")
        print("You can go on with the registration")
    if not isValidLen:
        print("Invalid Password: Passwords must be 8 to 16 characters long")
    if not hasSpecChar:
        print("Invalid Password: Passwords must contain all special characters (!, #)")
    if not hasNumber:
        print("Invalid Password: Passwords must contain a number")

if __name__ == "__main__":
    main()