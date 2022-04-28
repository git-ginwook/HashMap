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
        # lst = LinkedList()
        print(lst)
        lst.insert_back('C')
        lst.insert_back('B')
        lst.insert_back('A')
        lst.insert_back('A')
        lst.insert_back('A')
        print(lst)


if __name__ == '__main__':
    unittest.main()
