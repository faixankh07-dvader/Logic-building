def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    longest_sub = ""

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        current = s[left : right + 1]

        if len(current) > max_length:
            max_length = len(current)
            longest_sub = current

    return longest_sub, max_length


text = input("Enter a string: ")


def longest_substring_with_repeating(s):
    return s, len(s)


unique_sub, unique_len = longest_unique_substring(text)
repeat_sub, repeat_len = longest_substring_with_repeating(text)

print("Without repeating characters:")
print("Substring:", unique_sub)
print("Length:", unique_len)

print("\nWith repeating characters:")
print("Substring:", repeat_sub)
print("Length:", repeat_len)
