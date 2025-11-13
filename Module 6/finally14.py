def myFunction():
    try:
        raise Exception

    except TypeError:
        print("Error!")

    finally:
        print("Finally block has been executed!\n")

        return

# What is the output
def main():
    myFunction()

if __name__ == "__main__":
    main()