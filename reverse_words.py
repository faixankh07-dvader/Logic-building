# reverse words in sentence
string = input("Enter a string: ").split()
sresult = []

for s in reversed(string):
    sresult.append(s)

print(sresult)

# reverse string
sentence = input("Enter a string: ")

result = []

for char in reversed(sentence):
    result.append(char)

print("".join(result))  # join combine the words reversed in a string


# clean and reverse words


def reverse_words(sentence):
    words = sentence.split()

    seen = set()
    unique_words = []

    for word in words:
        if word not in seen:
            unique_words.append(word)
            seen.add(word)

    # Convert list to string
    return " ".join(reversed(unique_words))


user = input("ENTER A SENTENCE: ")
print(reverse_words(user))
