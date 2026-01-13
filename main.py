import random

# Helper Functions Up Here



# Main Function Here
def main():

    choices = ["rock", "paper", "scissors"]

    appOn = True

    while appOn:

        print("Let's play Rock, Paper, Scissors!")
        playerChoice = input("Make a move! (rock/paper/scissors) -> ").lower()
        compChoice = random.choice(choices)
        print(compChoice)

        if playerChoice == "rock" or playerChoice == "r":

            if compChoice == "rock":
                print(f"Computer chose {compChoice}! You tied!")
            elif compChoice == "paper":
                print(f"Computer chose {compChoice}! You lost!")
            else:
                print(f"Computer chose {compChoice}! You win!")

        elif playerChoice == "scissors" or playerChoice == "s":

            if compChoice == "rock":
                print(f"Computer chose {compChoice}! You lost!")
            elif compChoice == "paper":
                print(f"Computer chose {compChoice}! You win!")
            else:
                print(f"Computer chose {compChoice}! You tied!")

        elif playerChoice == "paper" or playerChoice == "p":

            if compChoice == "rock":
                print(f"Computer chose {compChoice}! You win!")
            elif compChoice == "paper":
                print(f"Computer chose {compChoice}! You tiet!")
            else:
                print(f"Computer chose {compChoice}! You lose!")

        else:
            print("That's not a move!")

        shutOff = input("Would you like to play again? (y/n) -> ").lower()
        if shutOff == "n" or shutOff == "no":
            appOn = False


# Main Call Here
main()