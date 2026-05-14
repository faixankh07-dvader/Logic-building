"""
num = input("Enter a number: ")
print("Reversed:", num[::-1])  # print(text[::-1]) moves backward through the string
"""

# reversing a number using loop
n = int(input("enter: "))
reverse = 0

while n > 0:
    digits = n % 10
    reverse = reverse * 10 + digits
    n = n // 10

print("Reversed number:", reverse)

# Check palindrome without slicing

word = input("Enter a word: ")

is_palindrome = True

start = 0
end = len(word) - 1 # len("madam")5 indexes start from 0, not 1. So the last index is: 5-1=4

while start < end:
    if word[start] != word[end]:
        is_palindrome = False
        break

    start += 1  # moves the pointer forward
    end -= 1  # moves the pointer backward.

if is_palindrome:
    print("palindrome")

else:
    print("Not palindrome")

#Palindrome Number (Without Converting to String)

num = int(input("Enter number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is not a palindrome")