class content:
    def __init__(self, text, media, likes = 1):
        self.text = text
        self.media = media
        self.likes = likes

# Class called user (template)
class user:
    user_amount = 0

    # Constructor Function
    # - Initialize the object/instance attributes
    def __init__(self, i, p, f = ""):
        self.id = i
        self.password = p
        self.prof_pic = f
        print(f"User {self.id} has been added.")
        user.user_amount += 1

def main():
    user_list = []

    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("[DEV]100. Print users")

        option = int(input("Select an option: "))

        if option == 1:
            pass
        elif option == 2:
            id = input("Enter id: ")
            password = input("Enter password: ")

            user_list.append(user(id, password))
        elif option == 100:
            for u in user_list:
                print(u.id)
        elif option == 3:
            break

if __name__ == "__main__":
    main()