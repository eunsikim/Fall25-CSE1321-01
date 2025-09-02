def main():
    # Non-Zero Numeric values resolve to `True` 
    number = 10

    print(number)
    print(bool(number))

    number = 0

    # Zero numeric values resolve to `False`
    print(number)
    print(bool(number))

    # Non-empty collection/sequence values resolve to `True` 
    message = "Hello World"
    print(message)
    print(bool(message))

    # Empty collection/sequence values resolve to `False`
    message = ""
    print(message)
    print(bool(message))

if __name__ == "__main__":
    main()