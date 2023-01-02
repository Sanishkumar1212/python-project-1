import tkinter as tk
import random

def play(user_choice):
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

# create the rock button
rock_button = tk.Button(window, image=rock_image, command=lambda: play('rock'))
rock_button.pack(side='left')

# create the paper button
paper_button = tk.Button(window, image=paper_image, command=lambda: play('paper'))
paper_button.pack(side='left')

# create the scissors button
scissors_button = tk.Button(window, image=scissors_image, command=lambda: play('scissors'))
scissors_button.pack(side='left')

# create the result label
result_text = tk.StringVar()
result_label = tk.Label(window, textvariable=result_text)
result_label.pack()

# load the images
rock_image = tk.PhotoImage(file='rock.png')
paper_image = tk.PhotoImage(file='paper.jpg')
scissors_image = tk.PhotoImage(file='scissors.jpg')

# start the event loop
window.mainloop()
