import random

def main():
    # Input and validation
    user_choice = input("Enter Rock, Paper, or Scissors: ")

    user_choice = user_choice.lower()

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Invalid choice")
    else:
        # Random Computer choice
        options = ['rock', 'paper', 'scissors']
        comp_choice = random.choice(options)

        print(f"Computer choice: {comp_choice}")

        # Logic
        # Win cases
        if user_choice == "rock":
            # Win
            if comp_choice == "scissors":
                print("Win")
            # Draw
            elif comp_choice == "rock":
                print("Draw")
            # Lost
            else:
                print("Lost")
        elif user_choice == "paper":
            # Win
            if comp_choice == "rock":
                print("Win")
            # Draw
            elif comp_choice == "paper":
                print("Draw")
            # Lost
            else:
                print("Lost")
        elif user_choice == "scissors":
        # Win
            if comp_choice == "paper":
                print("Win")
            # Draw
            elif comp_choice == "scissors":
                print("Draw")
            # Lost
            else:
                print("Lost")

if __name__ == "__main__":
    main()