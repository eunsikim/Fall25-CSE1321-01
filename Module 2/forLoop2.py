def main():
    hasNumber = False
    hasExcl = False
    hasHash = False

    password = input("Enter Password: ")

    for c in password:
        if c == "1" or c == "2" or c == "3" or c == "4" or c == "5" or c == "6" or c == "7" or c == "8" or c == "9" or c == "0":
            hasNumber = True
            break
    
    for c in password:
        if c == "!":
            hasExcl = True
        if c == "#":
            hasHash = True
    
    count = 0
    for c in password:
        count += 1
    
    if hasNumber and hasExcl and hasHash and (count >= 8):
        print("Your password is valid")
    else:
        print("Your password is not valid")

if __name__ == "__main__":
    main()