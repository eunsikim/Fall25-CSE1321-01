class test:
    number = 100

def main():
    t1 = test()
    t2 = test()

    t1.number = 5

    print(f"class: {test.number}")
    print(f"t1: {t1.number}")
    print(f"t2: {t2.number}")

if __name__ == "__main__":
    main()