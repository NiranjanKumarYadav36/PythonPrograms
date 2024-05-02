### reverse_sentence

punctuation = ['!', '%', '[', ']', '{', '}', '@', '$', '?']
text = input("Enter a sentence: ")

# Reverse the sentence
reversed_sentence = text[::-1]
print("Reversed sentence:", reversed_sentence)

new_text = ""

# Remove punctuation marks and build the new text
for char in reversed_sentence:
    if char not in punctuation:
        new_text = new_text + char

# Remove leading and trailing whitespace
new_text = new_text.strip()
print("Without punctuation and trimmed:", new_text)

# Capitalize the first letter
new_text = new_text.capitalize()
print("Capitalized:", new_text)
