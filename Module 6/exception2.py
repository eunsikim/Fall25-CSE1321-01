class NotEvenError(Exception):
    def __init__(self, message = ""):
        super().__init__(message)

def main():
    even_numbers = []

    # Filling the list
    while True:
        try:
            # POTENTIAL ISSUE: INCORRECT CONVERSION
            number = int(input("Enter an even number or -1 to stop: "))

            if number == -1:
                break 

            if number % 2 == 0:
                even_numbers.append(number)
                print("Number added successfully")
            else:
                raise NotEvenError(f"Please enter an even integer number, {number} is not even")
        except NotEvenError as error:
            print(error)
        except ValueError:
            print("Please enter an integer value number")
        except Exception:
            print("Error, contact developer")
        
        

    # Selection
    while True:
        try:
            for i in range(len(even_numbers)):
                print(f"{i} -> {even_numbers[i]}")
            
            # POTENTIAL ISSUE: INCORRECT CONVERSION
            index = int(input("Enter your selection or enter -1 to stop: "))
            if index == -1:
                break
            
            # POTENTIAL ISSUE: INDEX OUT OF BOUNDS
            print(f"You selected the number: {even_numbers[index]}")
        except ValueError:
            print("Please enter a correct index value number")
        except IndexError:
            print(f"Please enter an index value between 0 to {len(even_numbers) - 1}")
        except Exception:
            print("Error, contact developer")

if __name__ == "__main__":
    main()