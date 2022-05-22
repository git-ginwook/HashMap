import unittest
from min_heap import *


class TestMinHeap(unittest.TestCase):
    """ """
    def test_add(self):
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

    def test_is_empty(self):
        print("\nPDF - is_empty example 1")
        print("-------------------")
        h = MinHeap([2, 4, 12, 56, 8, 34, 67])
        print(h.is_empty())

        print("\nPDF - is_empty example 2")
        print("-------------------")
        h = MinHeap()
        print(h.is_empty())


if __name__ == '__main__':
    unittest.main()
