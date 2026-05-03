# smart number analyzer


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
    print("largest even ", largest_even)
    print("smallest odd ", smallest_odd)
    print("Final list", final_list)


nums = [4, 7, 2, 9, 4, 7, 6, 3]
smart_num_analyzer(nums)
