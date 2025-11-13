def myFunction():
    try:
        num = int("1.0")

        print("Try block executed successfully!")
    except ValueError:
        raise Exception
    except Exception:
        print("Catastrophic Error!")
    finally:
        print("\n\nFinally block has been executed!\n\n")

        return False
        

    return True

# What is the output
def main():
    if myFunction():
        print("Hello World")
    else:
        print("Hello CSE 1321")

if __name__ == "__main__":
    main()