## Replacing 'Python' with 'Java'
text = "Python empowers users to tackle a wide range of tasks, from web development and data analysis to artificial intelligence and scientific computing. Its popularity stems from its ability to streamline complex processes, allowing developers to focus on solving problems rather than wrestling with intricate syntax. Moreover, Python's"

text = text.replace(" Python ", " Java ")  # Replace whole words only
print(text)

## Counting vowels, consonants, and spaces
vowels = ['a', 'e', 'i', 'o', 'u']
count_vowels = 0
count_consonants = 0
spaces = 0

for char in text:
    if char.lower() in vowels:
        count_vowels += 1
    elif char.isalpha():
        count_consonants += 1
    elif char.isspace():
        spaces += 1

print('Count of consonants:', count_consonants)
print('Count of vowels:', count_vowels)
print('Count of spaces:', spaces)



## Checking for palindrome
text = "radar"
reversed_text = text[::-1]

if reversed_text == text:
    print("Palindrome")
else:
    print("Not a Palindrome")

## Counting occurrences of "Hello" in the text
text = "Hello i am niranjan i hello"
text = text.lower()
count_hello = text.count("hello")
print("Count of 'hello':", count_hello)
