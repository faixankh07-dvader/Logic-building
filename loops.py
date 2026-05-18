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


# Finds unique numbers in a list Without using set()

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
nums = [1, 2, 3, 2, 4, 7, 1]

unique = []

for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count += 1

    if count == 1:
        unique.append(nums[i])

print(unique)

# Which number appears the MOST times in the list.
num = [1, 2, 2, 3, 1, 2, 4]
max_count = 0
most_frequent = num[0]

for i in range(len(num)):
    count = 0
    for j in range(len(num)):
        if num[i] == num[j]:
            count += 1

    if count > max_count:
        max_count = count
        most_frequent = num[i]

print("Most frequent:", most_frequent)


#most frequent character in a string
text = input("Enter list of words: ")
max_count = 0
most_frequent_char = ""

for i in range(len(text)):
    count = 0
    for j in range(len(text)):
        if text[i] == text[j]:
            count += 1
    
    if count > max_count:
        max_count = count
        most_frequent_char = text[i]

print("Most frequent character: ", most_frequent_char)
