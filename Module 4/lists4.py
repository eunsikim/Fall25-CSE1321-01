def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    sub_states = states[::2]

    print(states[:2])

    print(states[2:5])

    print(states[0:6:2])
    print(states[::2])

    states.insert(9, "Washington")
    print(states)

    

if __name__ == "__main__":
    main()