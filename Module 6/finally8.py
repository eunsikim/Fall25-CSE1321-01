# What is the output
def main():
    try:
        num = int("1.0")

        print("Try block executed successfully!")
    except ValueError:
        raise Exception
    except Exception:
        print("Catastrophic Error!")
    finally:
        print("\n\nFinally block has been executed!\n\n")

        raise ZeroDivisionError

if __name__ == "__main__":
    main()