from random import choice
from time import sleep
from tabulate import tabulate

def print_dec(value, delay=0.01):
    for char in str(value):
        print(char, end="", flush=True)
        sleep(delay)
    

def random_choice():
    random_choice = choice(["rock", "paper", "scissors"]) 
    return random_choice

def tabulate_data(headers, data):
    table = tabulate(data, headers=headers, tablefmt="rounded_grid", stralign="center", numalign="center")
    print(table)

def get_winner(player, computer):
    if player == computer:
        return "Tie"
    elif player == "rock":
        if computer == "paper":
            return "Computer"
        else:
            return "Player"
    elif player == "paper":
        if computer == "scissors":
            return "Computer"
        else:
            return "Player"
    elif player == "scissors":
        if computer == "rock":
            return "Computer"
        else:
            return "Player"
        


def main():
    """
Welcome to this Rock 🪨, Paper 📃, Scissors ✂️ Game

You have 5 chances to win the game. The only
way to win is to beat the computer.

The rules are the same as Rock, Paper, Scissors i.e.
Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.

To Quit the game just type "quit" or "exit"
"""
    
    print_dec(main.__doc__)
    attempts = 0
    wins = 0
    losses = 0
    
    game_data = []
    headers = ["Attempt", "Computer", "Player", "Winner"]
    
    while attempts < 5:
        print(f"\nYou have {5 - attempts} attempts left")
        player = input("Rock, Paper, Scissors: ").lower()
        computer = random_choice()
        attempts += 1
        if player == "rock" or player == "paper" or player == "scissors":
            if player == computer:
                print(f"You chose {player} and the computer chose {computer}")
                print("It's a tie\n")
                winner = get_winner(player, computer)
            elif player == "rock" and computer == "scissors":
                print(f"You chose {player} and the computer chose {computer}")
                print("You win\n")
                wins += 1
                winner = get_winner(player, computer)
            elif player == "scissors" and computer == "paper":
                print(f"You chose {player} and the computer chose {computer}")
                print("You win\n")
                wins += 1
                winner = get_winner(player, computer)
            elif player == "paper" and computer == "rock":
                print(f"You chose {player} and the computer chose {computer}")
                print("You win\n")
                wins += 1
                winner = get_winner(player, computer)
            else:
                print(f"You chose {player} and the computer chose {computer}")
                print("Computer wins\n")
                losses += 1
                winner = get_winner(player, computer)
        elif player.startswith("q") or player.startswith("e"):
            print_dec("\nThank you for playing the game. Hope to see you again!! 😉😉")
            break
        else:
            print("Invalid input\n")
            attempts -= 1
            continue
        game_data.append([attempts, computer, player, winner])
    if attempts == 5:
        print("Game Over\n")
        tabulate_data(headers, game_data)
        print()

        if wins > losses:
            winRate = wins / (wins + losses) * 100
            print("You won the game")
        elif wins < losses:
            winRate = wins / (wins + losses) * 100
            print("You lost the game")
        else:
            winRate = 0
            print("The game was a tie")
        
        print_dec(f"You won {wins} times and lost {losses} times and your winrate was {winRate:.1f}%", 0.05)
        player = input("\nWould you like to play again? (y/n): ").lower()
        if player.startswith("y"):
            main()
        else:
            print_dec("\nThank you for playing the game. Hope to see you again!! 😉😉", 0.05)
            exit()
if __name__ == "__main__":
    main()