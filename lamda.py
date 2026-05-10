"""
Create a new list where:

odd numbers → multiplied by 3
even numbers → divided by 2
"""

nums = [5, 12, 7, 20]

result = list(map(lambda x: x / 2 if x % 2 == 0 else x * 3, nums))

print(result)

"""
even → square it
odd → subtract 5
"""
numlist = [10, 15, 8, 21]

result2 = list(map(lambda x: x**2 if x % 2 == 0 else x - 5, numlist))
print(result2)

"""
if negative → convert to positive
else if positive even → divide by 2
else if positive odd → multiply by 3


nums2 = [12, -5, 7, -8, 15]
absolute_value = [abs(num) for num in nums2]
result3 = list(map(lambda x: x / 2 if x % 2 == 0 else x * 3, absolute_value))
print(result3)
"""
"""
if negative → just absolute value
else if positive even → divide by 2
else if positive odd → multiply by 3
"""

nums2 = [12, -3, 9, -4, -1, 86]

result3 = list(
    map(lambda x: abs(x) if x < 0 else x / 2 if x % 2 == 0 else x * 3, nums2)
)
print(result3)
