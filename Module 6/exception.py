def main():
    while True:
        try:
            num = int(input("Enter a number: "))

            print(f"You entered the number: {num}")
        except ValueError:
            print("Please enter an integer value number")


if __name__ == "__main__":
    main()