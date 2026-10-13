#======================================================================
#   Project    5:       Number guessing  game   
#======================================================================

import random

number = random.randint(1, 10)

print("Number guess karo (1 se 10 ke beech)")

while True:
    guess = int(input("Aap ka guess: "))

    if guess < number:
        print("Bohat chota hai, dobara try karo")
    elif guess > number:
        print("Bohat bara hai, dobara try karo")
    else:
        print("Shabash! Aap ne sahi guess kiya!")
        break