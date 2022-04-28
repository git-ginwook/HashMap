import unittest
from sll import *


class TestAssignment(unittest.TestCase):
    def test_insert_front_back(self):
        print('\n# insert_front example 1')
        lst = LinkedList()
        print(lst)
        lst.insert_front('A')
        lst.insert_front('B')
        lst.insert_front('C')
        print(lst)

        print(lst.length())

        print('\n# insert_back example 1')
        lst = LinkedList()
        print(lst)
        lst.insert_back('C')
        lst.insert_back('B')
        lst.insert_back('A')
        lst.insert_back('A')
        lst.insert_back('A')
        print(lst)

    def test_insert_at_index(self):
        print('\n# insert_at_index example 1')
        lst = LinkedList()
        test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F'),
                      (1, 'X')]
        for index, value in test_cases:
            print('Insert of', value, 'at', index, ': ', end='')
            try:
                lst.insert_at_index(index, value)
                print(lst)
            except Exception as e:
                print(type(e))

    def test_remove_at_index(self):
        print('\n# remove_at_index example 1')
        lst = LinkedList([1, 2, 3, 4, 5, 6])
        print(lst)
        for index in [0, 0, 0, 2, 2, -2]:
            print('Removed at index:', index, ': ', end='')
            try:
                lst.remove_at_index(index)
                print(lst)
            except Exception as e:
                print(type(e))
        print(lst)

        # remove the last node
        lst = LinkedList([1, 2, 3, 4, 5, 6])
        lst.remove_at_index(5)
        print(lst)

    def test_remove(self):
        print('\n# remove example 1')
        lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
        print(lst)
        for value in [7, 3, 3, 3, 3]:
            print(lst.remove(value), lst.length(), lst)

        print('\n# remove example 2')
        lst = LinkedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
        print(lst)
        for value in [1, 2, 3, 1, 2, 3, 3, 2, 1]:
            print(lst.remove(value), lst.length(), lst)

    def test_count(self):
        print('\n# count example 1')
        lst = LinkedList([1, 2, 3, 1, 2, 2, 1])
        print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

        lst = LinkedList()
        print(lst, lst.count(2))

        lst = LinkedList([1])
        print(lst, lst.count(2), lst.count(1))


if __name__ == '__main__':
    unittest.main()
