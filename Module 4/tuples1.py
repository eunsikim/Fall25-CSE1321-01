def main():
    states = ("Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina")

    for state in states:
        print(state)

    states_list = list(states)

    del states_list[0]

    states = tuple(states_list)
    print(states)

    

if __name__ == "__main__":
    main()