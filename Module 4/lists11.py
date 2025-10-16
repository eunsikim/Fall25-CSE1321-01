def main():
    states = ["Georgia", "Florida", "Carolina", "Alabama", "Tennessee", "Carolina"]

    print(f"Carolina appears {states.count("Carolina")} times in the list")

    print(f"The first Carolina is at index {states.index("Carolina")}")
    print(states[0])
    states.reverse()
    print(states[0])

    print(states)

    states.sort()

    print(states)

    print(states[0])

    print(max(states))
    print(min(states))


    

if __name__ == "__main__":
    main()