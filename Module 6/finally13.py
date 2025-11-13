def myFunction():
    try:
        for i in range(5):
            if i == 2:
                raise TypeError
            else:
                print(f"i = {i}")

    except TypeError:
        print("Error!")
    finally:
        print("Finally block has been executed!\n")
    

# What is the output
def main():
    myFunction()
    print("[Program Terminated]")

if __name__ == "__main__":
    main()