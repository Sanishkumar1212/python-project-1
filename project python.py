import tkinter as tk
from tkinter import messagebox
import random

# list of possible choices
choices = ['rock', 'paper', 'scissors']

# function to determine the winner
def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return 'Tie'
  elif user_choice == 'rock' and computer_choice == 'scissors':
    return 'User'
  elif user_choice == 'paper' and computer_choice == 'rock':
    return 'User'
  elif user_choice == 'scissors' and computer_choice == 'paper':
    return 'User'
  else:
    return 'Computer'

# function to start the game
def start_game():
  user_choice = user_choice_str.get()
  computer_choice = random.choice(choices)

  result = determine_winner(user_choice, computer_choice)

  if result == 'Tie':
    messagebox.showinfo('Result', 'Tie!')
  elif result == 'User':
    messagebox.showinfo('Result', 'You won!')
  else:
    messagebox.showinfo('Result', 'Computer won!')

# create the main window
window = tk.Tk()
window.title('Rock Paper Scissors')

# create a label for instructions
instructions_label = tk.Label(window, text='Choose your option:')
instructions_label.pack()

# create a StringVar to store the user's choice
user_choice_str = tk.StringVar(window)

# create a dropdown menu for user to select their choice
user_choice_menu = tk.OptionMenu(window, user_choice_str, *choices)
user_choice_menu.pack()

# create a button to start the game
start_button = tk.Button(window, text='Start game', command=start_game)
start_button.pack()

# run the main loop
window.mainloop()
