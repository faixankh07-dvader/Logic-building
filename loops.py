"""
# Print each character of a word
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

# multiplication generator

i = int(input("Enter a number: "))

for j in range(1, 11):
    print(f"{i} x {j} = {i * j}")
"""

List1 = [1, 2, 3, 4]
List2 = [3, 4, 5, 6]

common = []

for num1 in List1:
    for num2 in List2:
        if num1 == num2:
            common.append(num1)

print(common)


rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("&", end="")

    print()
