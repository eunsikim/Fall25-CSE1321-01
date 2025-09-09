def main():
    str1 = "Hello World"
    str2 = "hello world"

    # str1 = str1.upper()
    # str2 = str2.upper()

    if str1.lower() == str2.lower():
        print("They are the same")
    else:
        print("They are different") 

if __name__ == "__main__":
    main()