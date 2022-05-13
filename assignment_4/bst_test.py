import unittest
from bst import *


class TestBST(unittest.TestCase):
    """ """
    def test_add(self):
        print("\nPDF - method add() example 1")
        print("----------------------------")
        test_cases = (
            (1, 2, 3),
            (3, 2, 1),
            (1, 3, 2),
            (3, 1, 2),
        )
        for case in test_cases:
            tree = BST(case)
            print(tree)

        print("\nPDF - method add() example 2")
        print("----------------------------")
        test_cases = (
            (10, 20, 30, 40, 50),
            (10, 20, 30, 50, 40),
            (30, 20, 10, 5, 1),
            (30, 20, 10, 10, 1, 5),
            (5, 4, 6, 3, 7, 2, 8),
            (range(0, 30, 3)),
            (range(0, 31, 3)),
            (range(0, 34, 3)),
            (range(10, -10, -2)),
            ('A', 'B', 'C', 'D', 'E'),
            (1, 1, 1, 1),
        )
        for case in test_cases:
            tree = BST(case)
            print('INPUT  :', case)
            print('RESULT :', tree)

        print("\nPDF - method add() example 3")
        print("----------------------------")
        for _ in range(100):
            case = list(set(random.randrange(1, 20000) for _ in range(900)))
            tree = BST()
            for value in case:
                tree.add(value)
            if not tree.is_valid_bst():
                raise Exception("PROBLEM WITH ADD OPERATION")
        print('add() stress test finished')

    def test_remove(self):
        print("\nPDF - method remove() example 1")
        print("-------------------------------")
        test_cases = (
            ((1, 2, 3), 1),
            ((1, 2, 3), 2),
            ((1, 2, 3), 3),
            ((50, 40, 60, 30, 70, 20, 80, 45), 0),
            ((50, 40, 60, 30, 70, 20, 80, 45), 45),
            ((50, 40, 60, 30, 70, 20, 80, 45), 40),
            ((50, 40, 60, 30, 70, 20, 80, 45), 30),
        )
        for case, del_value in test_cases:
            tree = BST(case)
            print('INPUT  :', tree, "DEL:", del_value)
            tree.remove(del_value)
            print('RESULT :', tree)

        print("\nPDF - method remove() example 2")
        print("-------------------------------")
        test_cases = (
            ((50, 40, 60, 30, 70, 20, 80, 45), 20),
            ((50, 40, 60, 30, 70, 20, 80, 15), 40),
            ((50, 40, 60, 30, 70, 20, 80, 35), 20),
            ((50, 40, 60, 30, 70, 20, 80, 25), 40),
        )
        for case, del_value in test_cases:
            tree = BST(case)
            print('INPUT  :', tree, "DEL:", del_value)
            tree.remove(del_value)
            print('RESULT :', tree)

        print("\nPDF - method remove() example 3")
        print("-------------------------------")
        case = range(-9, 16, 2)
        tree = BST(case)
        for del_value in case:
            print('INPUT  :', tree, del_value)
            tree.remove(del_value)
            print('RESULT :', tree)

        print("\nPDF - method remove() example 4")
        print("-------------------------------")
        case = range(0, 34, 3)
        tree = BST(case)
        for _ in case[:-2]:
            root_value = tree.get_root().value
            print('INPUT  :', tree, root_value)
            tree.remove(root_value)
            if not tree.is_valid_bst():
                raise Exception("PROBLEM WITH REMOVE OPERATION")
            print('RESULT :', tree)


class TestAVL(unittest.TestCase):
    """ """
    def test_something(self):
        pass


if __name__ == '__main__':
    unittest.main()
