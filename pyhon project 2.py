import tkinter as tk
import random

def play(choice):
    # get the computer's choice
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # determine the winner
    if choice == computer_choice:
        result_text.set("It's a tie!")
    elif (choice == 'rock' and computer_choice == 'scissors') or (choice == 'paper' and computer_choice == 'rock') or (choice == 'scissors' and computer_choice == 'paper'):
        result_text.set("You win!")
    else:
        result_text.set("You lose :(")

# create the main window
window = tk.Tk()
window.title("Rock Paper Scissors")

# create the rock button
tk.Button(window, text="Rock", command=lambda: play('rock')).pack()

# create the paper button
tk.Button(window, text="Paper", command=lambda: play('paper')).pack()

# create the scissors button
tk.Button(window, text="Scissors", command=lambda: play('scissors')).pack()

# create the result label
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

# start the event loop
window.mainloop()
