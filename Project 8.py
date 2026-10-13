#=============================================================
#     Project  8:    Rock,Paper,Scissor
#=============================================================

import random

print("Rock, Paper, Scissors game")
print("Likho: rock, paper ya scissors")

user = input("Aap ka choice: ").lower()
computer = random.choice(["rock", "paper", "scissors"])

if user != "rock" and user != "paper" and user != "scissors":
    print("Galat choice! Sirf rock, paper ya scissors likho")
else:
    print("Computer ne chuna:", computer)

    if user == computer:
        print("Barabar! Draw ho gaya")
    elif user == "rock" and computer == "scissors":
        print("Aap jeet gaye!")
    elif user == "paper" and computer == "rock":
        print("Aap jeet gaye!")
    elif user == "scissors" and computer == "paper":
        print("Aap jeet gaye!")
    else:
        print("Computer jeet gaya!")
        