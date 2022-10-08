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
            print(h, h.get_min())

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

    def test_get_min(self):
        print("\nPDF - get_min example 1")
        print("-----------------------")
        h = MinHeap(['fish', 'bird'])
        print(h)
        print(h.get_min(), h.get_min())

    def test_remove_min(self):
        print("\nPDF - remove_min example 1")
        print("--------------------------")
        h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
        while not h.is_empty() and h.is_empty() is not None:
            print(h, end=' ')
            print(h.remove_min())

    def test_build_heap(self):
        print("\nPDF - build_heap example 1")
        print("--------------------------")
        da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
        h = MinHeap(['zebra', 'apple'])
        print(h)
        h.build_heap(da)
        print(h)

        print("--------------------------")
        print("Inserting 500 into input DA:")
        da[0] = 500
        print(da)

        print("Your MinHeap:")
        print(h)
        if h.get_min() == 500:
            print("Error: input array and heap's underlying DA reference same object in memory")

    def test_size_clear(self):
        print("\nPDF - size example 1")
        print("--------------------")
        h = MinHeap([100, 20, 6, 200, 90, 150, 300])
        print(h.size())

        print("\nPDF - size example 2")
        print("--------------------")
        h = MinHeap([])
        print(h.size())

        print("\nPDF - clear example 1")
        print("---------------------")
        h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
        print(h)
        print(h.clear())
        print(h)

    def test_heapsort(self):
        print("\nPDF - heapsort example 1")
        print("------------------------")
        da = DynamicArray([100, 100, 20, 6, 100, 200, 90, 150, 300, 300])
        print(f"Before: {da}")
        heapsort(da)
        print(f"After:  {da}")

        print("\nPDF - heapsort example 2")
        print("------------------------")
        da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
        print(f"Before: {da}")
        heapsort(da)
        print(f"After:  {da}")


if __name__ == '__main__':
    unittest.main()
