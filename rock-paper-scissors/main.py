from utils.game_logic import get_computer_choice, decide_winner

def get_max_score():
        while True:
            max_score = input("Play to how many wins? (3 or 5): ")

            if max_score in ("3", "5"):
                return int(max_score)
            else:
                print("Invalid choice. Please enter 3 or 5.")


def get_player_choice(options):
        player = None

        while player not in options:
            player = input("Enter your choice (rock, paper, scissors): ").lower()

            if player not in options:
                print("Invalid choice. Please try again.")

        return player


def print_score(player_score, computer_score):
        print(f"Score → Player: {player_score} | Computer: {computer_score}")


def main():

    options = ("rock", "paper", "scissors")

    player_score = 0
    computer_score = 0
    round_number = 1


    print("=== ROCK PAPER SCISSORS ===")

    max_score = get_max_score()

    print(f"\nFirst to {max_score} wins!\n")

    while player_score < max_score and computer_score < max_score:
        print(f"\n----- ROUND {round_number} -----")

        player = get_player_choice(options)
        computer = get_computer_choice(options)

        print(f"Player: {player}")
        print(f"Computer: {computer}")

        result = decide_winner(player, computer)

        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1

        print_score(player_score, computer_score)
        round_number += 1


    print(f"\nFinal Score → Player: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("You won the game!")
    else:
        print("Computer won the game!")

    print("\nThanks for playing!")

if __name__ == "__main__":
    main()