import random

# Game rules
RULES = {
    ("Rock", "Paper"): "Paper",
    ("Rock", "Scissors"): "Rock",
    ("Paper", "Scissors"): "Scissors"
}

CHOICES = {1: "Rock", 2: "Paper", 3: "Scissors"}

print('Winning rules of ROCK PAPER SCISSORS:\n'
      'Rock vs Paper -> Paper wins\n'
      'Rock vs Scissors -> Rock wins\n'
      'Paper vs Scissors -> Scissors wins\n')

while True:
    print("\nEnter your choice:\n1 - Rock\n2 - Paper\n3 - Scissors")

    # User choice input and validation
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in CHOICES:
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    user_choice = CHOICES[choice]
    print(f"User choice: {user_choice}")

    # Computer choice
    comp_choice = CHOICES[random.randint(1, 3)]
    print(f"Computer choice: {comp_choice}")

    # Determine winner
    if user_choice == comp_choice:
        print("<== It's a tie! ==>")
    else:
        winner = RULES.get((user_choice, comp_choice)) or RULES.get((comp_choice, user_choice))
        print(f"<== {winner} wins! ==>")
        print("<== You win! ==>") if winner == user_choice else print("<== Computer wins! ==>")

    # Replay prompt
    if input("Do you want to play again? (Y/N): ").strip().lower() != 'y':
        break

print("Thanks for playing!")
