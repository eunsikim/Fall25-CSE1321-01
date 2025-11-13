# What is the output
def main():
    try:
        num = int("34.5")
        
        print("Try block executed successfully!")
    except TypeError:
        print("Error!")
    except Exception:
        print("Catastrophic Error!")

if __name__ == "__main__":
    main()