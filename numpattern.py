"""
Write a function that:
Takes a list of integers
Keeps only numbers that:
Are divisible by 3
AND whose digits sum to more than 10
"""

"""
def digit_sum(n):
    return sum(int(d) for d in (str(abs(n))))


def filter_number(nums):
    result = []

    for num in nums:
        if num % 3 == 0 and digit_sum(num) > 10:
            result.append(num)
    return result


nums = list(map(int, input("Enter numbers: ").split()))
for num in filter_number(nums):
    print(num)
"""
# similar code but with condition digit sum > 2 and num must be even


def digit_subtract(n):

    digits = [int(d) for d in str(abs(n))]

    result = digits[0]
    for d in digits[1:]:
        result -= d

    return result


def filter_number(nums):

    result = []

    for num in nums:
        if num % 2 == 0 and digit_subtract(num) > 2:
            result.append(num)
    return result


nums = list(map(int, input("Enter numbers: ").split()))
print(filter_number(nums))

"""
LOGIC EXPLANATION OF ABOVE CODE:

abs(n): converts the number in positive if its negative
str(abs(n)): convet the digit into string for looping as in python don't directly loop through digits
[int(d) for d in ...]: as d is a string so convert it into integer 

Step-by-step for n = 582:
abs(582) → 582
str(582) → "582"
Loop: '5', '8', '2'
Convert: 5, 8, 2
"""
