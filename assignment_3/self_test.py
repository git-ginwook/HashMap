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

        # test zero for zero


if __name__ == '__main__':
    unittest.main()
