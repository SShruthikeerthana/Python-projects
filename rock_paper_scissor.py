import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃'}
choices = tuple(emojis.keys())

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

score = {"wins": 0, "losses": 0, "ties": 0}

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print(f"{YELLOW}⚠️ Invalid choice! Please enter r, p, or s.{RESET}")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"{YELLOW}🤝 It's a tie!{RESET}")
        score["ties"] += 1
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print(f"{GREEN}🔥 You win this round!{RESET}")
        score["wins"] += 1
    else:
        print(f"{RED}💀 You lose this round.{RESET}")
        score["losses"] += 1

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    print("Rules: r = 🪨, p = 📃, s = ✂️\n")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)
        
        print(f"📊 Score → Wins: {score['wins']}, Losses: {score['losses']}, Ties: {score['ties']}\n")
        
        should_continue = input("Continue? (y/n): ").lower()
        if should_continue == "n":
            print("\n👋 Thanks for playing....Final Score:")
            print(f" Wins: {score['wins']} |  Losses: {score['losses']} | Ties: {score['ties']}")
          
          
            if score['wins'] > score['losses'] and score['wins'] > score['ties']:
                print(f"{GREEN}🏆 You WON the game! 🎉{RESET}")
            else:
                print(f"{RED}😢 You didn’t make it! Better luck next time.{RESET}")
            break  

play_game()
