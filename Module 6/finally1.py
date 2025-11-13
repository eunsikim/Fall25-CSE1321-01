# What is the output
def main():
    try:
        num = int("3.14")
        
        print("Try block executed successfully!")
    except Exception:
        print("Catastrophic Error!")
    except ValueError:
        print("Error!")

if __name__ == "__main__":
    main()