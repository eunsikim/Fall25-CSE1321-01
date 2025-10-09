def main():
    # We wqait for the user to enter a card
    # Validate credentials
    # Prompt some options
    # Ask the user if they want to do something else
    # If so, print receipt then give card back
    # if not, repeat from line 4

    while True:
        input("Enter card (press enter)...")

        if validateUser():
            printMenu()
            option = getUserOption()

            if option == 1:
                withdrawal()
            elif option == 2:
                deposit()
            elif option == 3:
                balance()
            elif option == 4:
                printReceipt()
                getCardBack()
                break
        else:
            print("Error")

    