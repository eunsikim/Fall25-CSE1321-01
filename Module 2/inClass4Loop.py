import random

def main():
    user_score = 0
    comp_score = 0

    while True:
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
            if user_choice == "rock" and comp_choice == "scissors":
                print("Win")
                user_score += 1
            elif user_choice == "paper" and comp_choice == "rock":
                print("Win")
                user_score += 1
            elif user_choice == "scissors" and comp_choice == "paper":
                print("Win")
                user_score += 1
            # Draw
            elif user_choice == comp_choice:
                print("Draw")
            # Lost
            else:
                print("Lost")
                comp_score += 1
        
        print(f"SCORE\nUSER:{user_score}\nCOMPUTER:{comp_score}")

        # CHALLENGE: MAKE SURE THE PROGRAM RUNS ANOTHER RUN ONLY IF THE USER ENTERS "yes"
        anotherGame = input("Do you want to play again (yes/no): ").lower()

        if anotherGame == "no":
            break
    
    print("Program Terminated")
        

if __name__ == "__main__":
    main()