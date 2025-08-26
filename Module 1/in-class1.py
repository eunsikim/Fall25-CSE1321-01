def main():
    earth_weight = float(input("Weight?: ")) # Converting input to float

    moon_weight = earth_weight * 0.165

    print("Your moon weight is ", end="")
    print(moon_weight)

if __name__ == "__main__":
    main()