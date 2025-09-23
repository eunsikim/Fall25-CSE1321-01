def main():
    for y in range(4):
        for x in range(10):
            if x == 5:
                break
            print(x, end="")
        print()


if __name__ == "__main__":
    main()