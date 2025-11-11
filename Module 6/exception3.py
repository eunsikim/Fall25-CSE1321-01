class Not24HourValueError(Exception):
    def __init__(self, message = ""):
        super().__init__(message)

def main():
    # try:
        hour = int(input("Enter a 24-hour value to convert: "))

        if hour > 23 or hour < 0:
            raise Not24HourValueError("Please enter a value between 0 and 23")
        if hour > 12:
            hour -= 12
    
        print(f"That's {hour} hours in the 12-hour system")
    # except ZeroDivisionError as error:
    #     print(error)
    # except ValueError:
    #     print("Please enter an integer value")

if __name__ == "__main__":
    main()