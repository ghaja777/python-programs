# Ask the user for input to create a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse the order of words
reversed_sentence = ' '.join(reversed(words))

# Print the reversed sentence
print("Reversed Sentence:", reversed_sentence)
