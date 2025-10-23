def some_function():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    return (name, age)


def main():
    name_age_tuple = some_function()

    print(f"Name: {name_age_tuple[0]}, Age: {name_age_tuple[1]}")

    

if __name__ == "__main__":
    main()