def checker(number):
    print(f"while {number} <= 3 --- {number <= 3}")
    return True

def main():
    number = 0
    print(f"number = {number}")
    print()
    while checker(number) and number <= 3:
        # print(f"while {number} <= 3 --- {number <= 3}")
        print(f"Iteration #{number}")

        print(f"number = {number} + 1 --- {number + 1}")
        number += 1

        print()

if __name__ == "__main__":
    main()