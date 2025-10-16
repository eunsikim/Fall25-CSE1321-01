def main():
    states = ("Georgia", "Florida", "Alabama")
    more_states = ("Tennessee", "S. Carolina", "N. Carolina")

    states += more_states
    print(states)

    states_1 = states[0:3]
    states_2 = states[3:]

    print(states)
    print(states_1)
    print(states_2)

    

if __name__ == "__main__":
    main()