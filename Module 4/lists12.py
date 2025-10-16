def main():
    states = ["Georgia", "Florida", "Alabama", "Tennessee", "S. Carolina", "N. Carolina"]

    str_states = "\n".join(states)

    print(str_states)

    temps_str = "70,78,80,90,91"

    temps_list = temps_str.split(",")

    print(temps_list)

    for temperature in temps_list:
        print(temperature)





    

if __name__ == "__main__":
    main()