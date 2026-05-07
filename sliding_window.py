def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    longest_sub = ""

    # Remove characters until no duplicate remains
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


# 2. Longest substring WITH repeating characters
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

# ANOTHER PRACTICE CODE FOR SLIDING WINDOW TECHNIQUE


def max_sum_subarray(arr, k):

    # Sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        # Add new element and remove old element
        window_sum = window_sum + arr[i] - arr[i - k]

        # Update maximum sum
        if window_sum > max_sum:
            max_sum = window_sum

    return max_sum


# User input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter window size: "))

result = max_sum_subarray(numbers, k)

print("Maximum sum:", result)
