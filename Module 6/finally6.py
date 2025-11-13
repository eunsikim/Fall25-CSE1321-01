# What is the output
def main():
    try:
        num = int("10")

        print("Try block executed successfully!")
    except Exception:
        print("Catastrophic Error!")
    finally:
        print("\n\nFinally block has been executed!\n\n")

if __name__ == "__main__":
    main()