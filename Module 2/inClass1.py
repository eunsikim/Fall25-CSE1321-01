def main():
    age = int(input("Enter age: "))

    # if age >= 18:
    #     print("You can vote.")
    # else:
    #     print("You cannot vote yet.")

    if age < 18:
        print("You cannot vote yet.")
    else:
        print("You can vote.")

if __name__ == "__main__":
    main()