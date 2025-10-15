def main():
    states = ["Georgia", "Florida", "Alabama"]

    for s in states:
        print(s, end=" ")

    print()

    for i in range(len(states)):
        print(states[i])

    print()

    if "Georgia" in states:
        print("The list contains Georgia")
    else:
        print("The list does not contain Georgia")

if __name__ == "__main__":
    main()