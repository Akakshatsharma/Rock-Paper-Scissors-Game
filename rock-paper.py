import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.user_score = 0
        self.computer_score = 0

        # Label for user and computer choices
        self.user_choice_label = tk.Label(self.root, text="Your Choice:")
        self.user_choice_label.pack()

        self.computer_choice_label = tk.Label(self.root, text="Computer's Choice:")
        self.computer_choice_label.pack()

        # Buttons for user choices
        self.rock_button = tk.Button(self.root, text="Rock", width=10, command=lambda: self.play_game("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(self.root, text="Paper", width=10, command=lambda: self.play_game("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(self.root, text="Scissors", width=10, command=lambda: self.play_game("scissors"))
        self.scissors_button.pack(pady=5)

        # Label for game result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

        # Label for score
        self.score_label = tk.Label(self.root, text="Score - You: 0, Computer: 0")
        self.score_label.pack()

    def play_game(self, user_choice):
        """Function to play the game based on user's choice."""
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)

        # Update user and computer choice labels
        self.user_choice_label.config(text=f"Your Choice: {user_choice.capitalize()}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice.capitalize()}")

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1

        # Update result label and score label
        self.result_label.config(text=result)
        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")

    def reset_game(self):
        """Function to reset the game."""
        self.user_score = 0
        self.computer_score = 0
        self.user_choice_label.config(text="Your Choice:")
        self.computer_choice_label.config(text="Computer's Choice:")
        self.result_label.config(text="")
        self.score_label.config(text="Score - You: 0, Computer: 0")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
