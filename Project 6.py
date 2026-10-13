#=========================================================================
#    Project   6:          Simple   quize   app
#=========================================================================

score = 0

print("Quiz shuru!")

answer = input("1. Pakistan ka capital kya hai? ")
if answer.lower() == "islamabad":
    print("Sahi!")
    score = score + 1
else:
    print("Galat! Jawab Islamabad hai")

answer = input("2. 5 + 3 kitne hote hain? ")
if answer == "8":
    print("Sahi!")
    score = score + 1
else:
    print("Galat! Jawab 8 hai")

answer = input("3. Python kis cheez ka naam hai? (language/janwar) ")
if answer.lower() == "language":
    print("Sahi!")
    score = score + 1
else:
    print("Galat! Jawab language hai")

print("Quiz khatam! Aap ka score:", score, "/ 3")