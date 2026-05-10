"""
# Print each character of a word

# word = "Python"
word = input("enter a word: ")
result = []

for words in word:
    result.append(words)

print(result)

# print words tha has a or n in them

word1 = input("Enter list of words: ").split()   #split() breaks the string into a list of words using spaces

result1 = []
for w in word1:
    if "a" in w.lower() or "n" in w.lower():
        result1.append(w)

print(result1)
"""

# reverse words in sentence
string = input("Enter a string: ").split()

sresult = []

for s in reversed(string):
    sresult.append(s)

print(sresult)

# reverse string

string = input("Enter a string: ")

result = []

for char in reversed(string):
    result.append(char)

print("".join(result))  # join combine the words reversed in a string
