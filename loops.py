# Print each character of a word

# word = "Python"
word = input("enter a word: ")
result = []

for words in word:
    result.append(words)

print(result)

# print words tha has a or n in them

word1 = input("Enter list of words: ").split()

result1 = []
for w in word1:
    if "a" in w.lower() or "n" in w.lower():
        result1.append(w)

print(result1)
