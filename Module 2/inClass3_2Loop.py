def main():
    number = int(input("Enter a number: "))

    for n in range(1, number + 1):
        output = ""

        if n % 3 == 0:
            output += "Fizz"
        if n % 5 == 0:
            output += "Buzz"

        if output == "":
            output = str(n)
        
        print(output)

if __name__ == "__main__":
    main()