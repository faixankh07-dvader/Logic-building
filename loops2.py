"""
num = input("Enter a number: ")
print("Reversed:", num[::-1])  # print(text[::-1]) moves backward through the string
"""
'''
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
'''

#find the second largest number
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
largest = float('-inf')
sec_largest = float('-inf')

for num in numbers:
    if num > largest:
        sec_largest = largest
        largest = num 

    elif num > sec_largest and num != largest:
        sec_largest = num

print("Second largest number is:", sec_largest)

#find the second smallest number
numbers = [12, 45, 7, 89, 34]
smallest = float('inf')
second_smallest = float('inf')

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num

    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest number is:", second_smallest)

#find largest
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(f"{num} is the largest number")