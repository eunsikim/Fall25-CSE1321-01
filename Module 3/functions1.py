def helloWorld():
    print("Hello World")

def addition(num1, num2):
    op = num1 + num2

    return op

def printMenu():
    print("Press 1 for Hello World")
    print("Press 2 for Addition")
    print("Press X to quit")

    return input("> ")

def main():
    while True:
        option = printMenu()

        if option == "1":
            helloWorld()
        elif option == "2":
            num1 = int(input("Enter a number: "))
            num2 = int(input("Enter another number: "))

            print(addition(num1, num2))

            print("Hello World", end = ", ")
        elif option == "X":
            break

if __name__ == "__main__":
    main()