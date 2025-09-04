def main():
    number = int(input("Enter number: "))

    if number == 0:
        print("Your number is zero")
    elif number <= -1:
        print("Your number is negative")
    else:
        if number % 2 == 0:
            print("Your number is even")
        elif number % 2 == 1:
            print("Your number is odd")


if __name__ == "__main__":
    main()