import time

def main():
    # Parent Loop/Outer Loop
    for x in range(3):
        print(f"Parent Loop: Iteration #{x}")
        print("I am going to start working on the child loop...")
        time.sleep(1)

        # Child Loop/Inner Loop
        for y in range(5):
            print(f"\tChild Loop: Iteration #{y}")
            time.sleep(1)

        print("I am done working on the child loop...")
        time.sleep(1)


if __name__ == "__main__":
    main()