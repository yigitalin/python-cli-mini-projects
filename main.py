#ROCK, PAPER, SCISSORS v2.0
print("=== ROCK PAPER SCISSORS ===")

import random

options = ("rock", "paper", "scissors")

player_score = 0
computer_score = 0
round_number = 1

while True:
    max_score = input("Play to how many wins? (3 or 5): ")

    if max_score in ("3", "5"):
        max_score = int(max_score)
        break
    else:
        print("Invalid choice. Please enter 3 or 5.")

print(f"\nFirst to {max_score} wins!\n")

while player_score < max_score and computer_score < max_score:
    print(f"\n----- ROUND {round_number} -----")

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ").lower()
        if player not in options:
            print("Invalid choice. Please try again.")


    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score → Player: {player_score} | Computer: {computer_score}")
    round_number += 1

print(f"\nFinal Score → Player: {player_score} | Computer: {computer_score}")

if player_score > computer_score:
    print("You won the game!")
else:
    print("Computer won the game!")

print("\nThanks for playing!")