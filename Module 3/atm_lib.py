def validateUser():
    pin = input("Enter PIN#: ")

    if len(pin) == 4:
        # validation = getValidation(pin)
        if pin == "1234":
            return True
        else:
            return False
    else:
        False