"""
Create a new list where:

odd numbers → multiplied by 3
even numbers → divided by 2
"""

nums = [5, 12, 7, 20]

result = list(map(lambda x: x / 2 if x % 2 == 0 else x * 3, nums))

print(result)


numlist = [10, 15, 8, 21]

List = list(map(lambda x: x**2 if x % 2 == 0 else x - 5, numlist))
print(List)
