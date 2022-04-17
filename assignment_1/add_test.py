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
            [5, 5, 5, 5, 5, 5, 5],                              #
            [-5, -5, -3, -3, -3, 0, 0, 0, 0, 0, 5]              #
        )
        for case in test_cases:
            arr = StaticArray(len(case))
            for i, value in enumerate(case):
                arr[i] = value
            # print(arr)
            print(remove_duplicates(arr))
        # print(arr)


if __name__ == '__main__':
    unittest.main()
