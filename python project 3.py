import tkinter as tk
import random

def play():
    # get the user's choice
    user_choice = user_choice_var.get()

    # get the computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # determine the winner
    if user_choice == computer_choice:
        result_text.set("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'scissors' and computer_choice == 'paper'):
        result_text.set("You win!")
    else:
        result_text.set("You lose :(")

# create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# create the user choice radio buttons
user_choice_var = tk.StringVar()
tk.Button(window, text="Rock", command=play).pack()
tk.Button(window, text="Paper", command=play).pack()
tk.Button(window, text="Scissors", command=play).pack()

# create the play button
# tk.Button(window, text="Play", command=play).pack()

# create the result label
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

# start the event loop
window.mainloop()
