def main():
    # print("*" * 5)
    size = int(input("Enter a number: "))

    for row in range(size):
        # print("*" * size)
        for col in range(size):
            print("7", end="")
        print()

    counter = 1
    for row in range(size):
        for col in range(counter):
            print("*", end="")
        print()

        counter += 1

    es = size - 1
    a = 1

    for row in range(size):
        # Solution 1
        # for col in range(es):
        #     print(" ", end="")
        # for col in range(a):
        #     print("*", end="")

        # Solution 2
        for col in range(size):
            if col < es:
                print(" ", end="")
            else:
                print("*", end="")
        print()
        es -= 1
        a += 1

if __name__ == "__main__":
    main()