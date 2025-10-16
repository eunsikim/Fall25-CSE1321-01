def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    del states[2]
    print(states)

    print(f"We have deleted the state of {states.pop(2)}")
    print(f"The new value at index 2 is now the state of {states[2]}")
    print(states)

    

if __name__ == "__main__":
    main()