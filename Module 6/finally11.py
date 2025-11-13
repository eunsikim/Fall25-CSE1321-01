def myFunction():
    for i in range(10):
        try:
            if i == 5:
                raise TypeError
            else:
                print(f"i = {i}")

        except TypeError:
            break

# What is the output
def main():
    myFunction()

if __name__ == "__main__":
    main()