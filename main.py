# smart number analyzer
"""

def smart_num_analyzer(nums):

    unique_nums = list(set(nums))

    even = []
    odd = []

    for num in unique_nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    even.sort()
    odd.sort(reverse=True)

    largest_even = max(even) if even else None
    smallest_odd = min(odd) if odd else None

    final_list = even + odd

    print("Unique list: ", unique_nums)
    print("Even numbers: ", even)
    print("Odd numbers: ", odd)
    print("largest even: ", largest_even)
    print("smallest odd: ", smallest_odd)
    print("Final list", final_list)


nums = [4, 7, 2, 9, 4, 7, 6, 3]
smart_num_analyzer(nums)
"""


def smart_num_analyzer(nums):

    seen = set()
    unique_nums = []
    for num in nums:
        if num not in seen:
            unique_nums.append(num)
            seen.add(num)

    even = []
    odd = []

    for num in unique_nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    even_sort = sorted(even)
    odd_sort = sorted(odd, reverse=True)

    largest_even = max(even_sort) if even_sort else None
    smallest_odd = min(odd_sort) if odd_sort else None

    final_list = even_sort + odd_sort

    return {
        "Unique list ": unique_nums,
        "even_sort ": even_sort,
        "odd_sort ": odd_sort,
        "largest_even ": largest_even,
        "smallest_odd ": smallest_odd,
        "final_list ": final_list,
    }


user_input = input("Enters number separated by space ")

nums = list(map(int, user_input.split()))

result = smart_num_analyzer(nums)

for key, value in result.items():
    print(f"{key}: {value}")
