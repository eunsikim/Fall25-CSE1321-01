def myFunction():
    try:
        return None

    except Exception:
        print("Catastrophic Error!")

    finally:
        print("Finally block has been executed!\n")


# What is the output
def main():
    myFunction()
    print("[Program terminated]")

if __name__ == "__main__":
    main()