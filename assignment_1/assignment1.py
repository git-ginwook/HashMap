# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: Python Fundamentals Review
# Due Date: 4/18/2022
# Description:


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    """
    identify min and max of the input array
    return the values as a tuple: (min, max)
    """
    # set initial values of min and max
    arr_min, arr_max = arr[0], arr[0]

    # iterate through arr to identify min and max values
    for pos in range(1, arr.length()):
        # when the current value is smaller than min
        if arr[pos] < arr_min:
            arr_min = arr[pos]              # replace min

        # when the current value is greater than max
        if arr[pos] > arr_max:
            arr_max = arr[pos]              # replace max

    return arr_min, arr_max


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    create a new StaticArray object that modifies the original content:
    1) if the value is a multiple of 3, change to 'fizz'
    2) if the value is a multiple of 5, change to 'buzz'
    3) if the value is a multiple of both 3 and 5, change to 'fizzbuzz'

    return the new object with modified content
    """
    # create a temporary class object
    temp = StaticArray(arr.length())

    # iterate through 'arr' to replace values divisible by 3 or 5, or both
    for pos in range(arr.length()):
        # multiples of 15 (the Least Common Multiple of 3 and 5)
        if arr[pos] % 5 == 0 and arr[pos] % 3 == 0:
            temp.set(pos, 'fizzbuzz')          # 0 is also divisible by 3 and 5

        # multiples of 3
        elif arr[pos] % 3 == 0:
            temp.set(pos, 'fizz')

        # multiples of 5
        elif arr[pos] % 5 == 0:
            temp.set(pos, 'buzz')

        # fill in the remaining indices in temp
        else:
            temp.set(pos, arr[pos])

    return temp


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    reverse the order of original content in a given StaticArray object
    """
    # iterate through 'arr' to swap head and tail (move inward)
    for head_pos in range(int(arr.length() / 2)):
        head_to_tail = arr[head_pos]        # store the value of head

        tail_pos = arr.length()-head_pos-1  # identify tail position

        # swap head and tail
        arr.set(head_pos, arr[tail_pos])
        arr.set(tail_pos, head_to_tail)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
    rotate the array in 'arr' and place it in a new StaticArray object

    if 'steps' is positive, rotate clockwise
    if 'steps' is negative, rotate counter-clockwise

    return the new object
    """
    # create a new StaticArray object
    rot_arr = StaticArray(arr.length())

    # truncate steps to remove repeat rotations
    mod_steps = steps % arr.length()

    # iterate through 'arr' to place the rotated content in 'rot_arr'
    for pos in range(arr.length()):
        new_pos = (pos+mod_steps) % arr.length()
        rot_arr.set(new_pos, arr[pos])

    return rot_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    """
    TODO: Write this implementation
    """
    #
    size = abs(end-start)+1
    arr = StaticArray(size)

    #
    val = start

    #
    for pos in range(size):
        arr.set(pos, val)

        if start <= end:
            val += 1
        else:
            val -= 1

    return arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    # base case: only one value in 'arr'
    if arr.length() == 1:
        return 1

    val = 0                                 # set initial val
    #
    for pos in range(arr.length()-1):
        if arr[pos] < arr[pos+1]:           # ascending
            val += 1
            res = 1

        elif arr[pos] > arr[pos+1]:         # descending
            val -= 1
            res = -1

        else:                               # same values
            return 0

    if abs(val) != (arr.length()-1):
        return 0

    return res


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple:
    """
    TODO: Write this implementation
    """
    #
    mod = arr[0]
    freq = 1
    new = 1

    # base case:
    if arr.length() == 0:
        return mod, freq

    #
    for pos in range(1, arr.length()):
        #
        if arr[pos-1] == arr[pos]:
            new += 1

            #
            if freq < new:
                mod = arr[pos]
                freq = new

        #
        else:
            new = 1

    return mod, freq


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    #
    hold_arr = StaticArray(arr.length())
    hold_arr[0] = arr[0]

    # base case
    if arr.length() == 1:
        res_arr = StaticArray(1)
        res_arr[0] = hold_arr[0]
        return res_arr

    #
    num = 0

    #
    for pos in range(1, arr.length()):
        if arr[pos-1] != arr[pos]:
            num += 1
            hold_arr[num] = arr[pos]

    res_arr = StaticArray(num+1)

    for pos in range(num+1):
        res_arr[pos] = hold_arr[pos]

    return res_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # create 'count_arr'
    min, max = min_max(arr)
    length = abs(max-min)+1
    count_arr = StaticArray(length)

    # frequency
    for pos in range(arr.length()):
        insert_at = max - arr[pos]

        if count_arr[insert_at] is None:
            count_arr.set(insert_at, 0)
        count_arr[insert_at] += 1

    # accumulate
    accum = count_arr[0]

    #
    for pos in range(count_arr.length()-1):
        if count_arr[pos+1] is None:
            count_arr.set(pos+1, 0)
        accum = accum + count_arr[pos+1]
        count_arr.set(pos+1, accum)
    # count_arr[0] = 0

    # rotate
    count_arr = rotate(count_arr, 1)
    count_arr[0] = 0

    # result array
    sort_arr = StaticArray(arr.length())

    #
    for pos in range(arr.length()):
        locator = max - arr[pos]
        insert_at = count_arr[locator]
        sort_arr.set(insert_at, arr[pos])
        count_arr[locator] += 1

    return sort_arr


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
