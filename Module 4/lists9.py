def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    for i in range(len(states)):
        print(f"{i} {states[i]}")

    selection = int(input("Select the index you want remove: "))

    del states[selection]

    print()

    for state in states:
        print(state)


    

if __name__ == "__main__":
    main()