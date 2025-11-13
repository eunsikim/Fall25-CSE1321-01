# What is the output
def main():
    try:
        num = int("1.4")

        print("Try block executed successfully!")
    except ValueError:
        raise Exception


if __name__ == "__main__":
    main()