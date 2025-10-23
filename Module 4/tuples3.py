def some_function(*args, name, age):
    print(f"Name: {name}, Age: {age}")
    for i in args:
        print(i)

def some_other_function(my_tuple):
    for i in my_tuple:
        print(i)

def main():
    some_function(True, 1, 3.14, "Hello World", name="John", age=30)
    # some_other_function((True, 1, 3.14, "Hello World"))

    

if __name__ == "__main__":
    main()