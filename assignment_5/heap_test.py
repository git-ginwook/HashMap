import unittest
from min_heap import *


class TestMinHeap(unittest.TestCase):
    """ """
    def test_something(self):
        print("\nPDF - add example 1")
        print("-------------------")
        h = MinHeap()
        print(h, h.is_empty())
        for value in range(300, 200, -15):
            h.add(value)
            print(h)

        print("\nPDF - add example 2")
        print("-------------------")
        h = MinHeap(['fish', 'bird'])
        print(h)
        for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
            h.add(value)
            print(h)


if __name__ == '__main__':
    unittest.main()
