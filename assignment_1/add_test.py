import unittest
from assignment1 import *
from static_array import *


class TestAssignment(unittest.TestCase):
    def test_fizz_buzz(self):
        # wide range test
        source = [_ for _ in range(-40, 20, 1)]
        arr = StaticArray(len(source))
        for i, value in enumerate(source):
            arr[i] = value
        print(fizz_buzz(arr))
        print(arr)

        # single value test
        arr_2 = StaticArray(1)
        arr_2[0] = 55
        print(fizz_buzz(arr_2))
        print(arr_2)

    def test_reverse(self):
        # odd array size test
        source = [_ for _ in range(-10, 10, 4)]
        arr = StaticArray(len(source))
        for i, value in enumerate(source):
            arr.set(i, value)
        print(arr)
        reverse(arr)
        print(arr)
        reverse(arr)
        print(arr)

    def test_is_sorted(self):
        test_cases = (
            [1, 3, -10, 20, -30, 0],
            [-10, 0, 0, 10, 20, 30],
            [1, 2, 3, 4, 5, -6]
        )
        for case in test_cases:
            arr = StaticArray(len(case))
            for i, value in enumerate(case):
                arr[i] = value
            result = is_sorted(arr)
            space = "  " if result >= 0 else " "
            print(f"Result:{space}{result}, {arr}")

    def test_find_mode(self):
        test_cases = (
            [1, 20, 30, 40, 500, 500, 500],
            [2, 2, 2, 2, 1, 1, 1, 1],
            ["zebra", "sloth", "otter", "otter", "moose", "koala"],
            ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"],
            [-1, -1, -1, -1],               #
            [15, 15, 1, 3, 4, 4],           #
            [0],                            #
            ["GinWook"]                     #
        )
        for case in test_cases:
            arr = StaticArray(len(case))
            for i, value in enumerate(case):
                arr[i] = value

            mode, frequency = find_mode(arr)
            print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    def test_remove_duplicates(self):
        test_cases = (
            [1],
            [1, 2],
            [1, 1, 2],
            [1, 20, 30, 40, 500, 500, 500],
            [5, 5, 5, 4, 4, 3, 2, 1, 1],
            [1, 1, 1, 1, 2, 2, 2, 2],
            [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],               #
            [-5, -5, -3, -3, -3, 0, 0, 0, 0, 0, 5]              #
        )
        for case in test_cases:
            arr = StaticArray(len(case))
            for i, value in enumerate(case):
                arr[i] = value
            print(arr)
            print(remove_duplicates(arr))
        print(arr)

    def test_count_sort(self):
        test_cases = (
            # base case: one value
            [15],
            # negative values
            [-11, -10, -8, -5, -5, -1, 0, 0, 0, 14, 14, 15, 16, -11],
            [6, 6, 5, 4, 6, 4, 5, 1],
            [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
            [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
            [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001]

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

    def test_sorted_squares(self):
        test_cases = (
            [1, 2, 3, 4, 5],
            [-5, -4, -3, -2, -1, 0],
            [-3, -2, -2, 0, 1, 2, 3],
            # edge cases
            [-10, -3, -3, 1, 2, 3, 4, 4, 10],
            [1],
            [-1],
            [0],
            [0, 0]
        )
        for case in test_cases:
            arr = StaticArray(len(case))
            for i, value in enumerate(sorted(case)):
                arr[i] = value
            print(arr)
            result = sorted_squares(arr)
            print(result)


if __name__ == '__main__':
    unittest.main()
