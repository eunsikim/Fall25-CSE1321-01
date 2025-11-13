# What is the output
def main():
    try:
        num = int("1.0")

        print("Try block executed successfully!")
    except ZeroDivisionError:
        print("Catastrophic Error!")
    finally:
        print("\n\nFinally block has been executed!\n\n")
    

if __name__ == "__main__":
    main()