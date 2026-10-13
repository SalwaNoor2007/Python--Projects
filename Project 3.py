#====================================================================
#     Project    3:        Word Counter
#====================================================================

# Word Counter

# User se text lo
text = input("Apna text likho: ")

# Text ko words mein todo
words = text.split()

# Words ginो
total_words = len(words)

# Characters gino (spaces samet)
total_characters = len(text)

# Result dikhao
print("Total words:", total_words)
print("Total characters:", total_characters)