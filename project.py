import random
count1=0
count2=0
count3=0
while True:
    my_answer = input("Choose: rock, paper or scissors:\nChoose quit to quit the Game:\n")
    my_answer = my_answer.lower()

    if my_answer == "quit":
        print("Final Scores:")
        print("Computer:",count1)
        print("Player:",count2)
        print("Tie:",count3)
        break

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors":
        print("Please choose a correct answer")
        continue

    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_answer}")

    if my_answer == computer_answer:
        print("You tied")
        count3+=1
    elif my_answer == "paper" and computer_answer == "rock":
        print("YOU Win!")
        count2+=1
        
    elif my_answer == "rock" and computer_answer == "scissors":
        print("YOU Win!")
        count2+=1
        
    elif my_answer == "scissors" and computer_answer == "paper":
        print("YOU Win!")
        
        count2+=1
    else:
        print("You lose. Try again!")
        count1+=1
