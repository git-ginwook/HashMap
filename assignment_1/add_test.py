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


if __name__ == '__main__':
    unittest.main()