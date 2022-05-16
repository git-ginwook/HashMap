import unittest
from bst import *
from avl import *


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

    def test_contains(self):
        print("\nPDF - method contains() example 1")
        print("---------------------------------")
        tree = BST([10, 5, 15])
        print(tree.contains(15))
        print(tree.contains(-10))
        print(tree.contains(15))

        print("\nPDF - method contains() example 2")
        print("---------------------------------")
        tree = BST()
        print(tree.contains(0))

    def test_inorder(self):
        print("\nPDF - method inorder_traversal() example 1")
        print("---------------------------------")
        tree = BST([10, 20, 5, 15, 17, 7, 12])
        print(tree.inorder_traversal())

        print("\nPDF - method inorder_traversal() example 2")
        print("---------------------------------")
        tree = BST([8, 10, -4, 5, -1])
        print(tree.inorder_traversal())


class TestAVL(unittest.TestCase):
    """ """
    def test_add(self):
        print("\nPDF - method add() example 1")
        print("----------------------------")
        test_cases = (
            (1, 2, 3),  # RR
            (3, 2, 1),  # LL
            (1, 3, 2),  # RL
            (3, 1, 2),  # LR
        )
        for case in test_cases:
            tree = AVL(case)
            print(tree)

        print("\nPDF - method add() example 2")
        print("----------------------------")
        test_cases = (
            (10, 20, 30, 40, 50),  # RR, RR
            (10, 20, 30, 50, 40),  # RR, RL
            (30, 20, 10, 5, 1),  # LL, LL
            (30, 20, 10, 1, 5),  # LL, LR
            (5, 4, 6, 3, 7, 2, 8),  # LL, RR
            (range(0, 30, 3)),
            (range(0, 31, 3)),
            (range(0, 34, 3)),
            (range(10, -10, -2)),
            ('A', 'B', 'C', 'D', 'E'),
            (1, 1, 1, 1),
        )
        for case in test_cases:
            tree = AVL(case)
            print('INPUT  :', case)
            print('RESULT :', tree)

        print("\nPDF - method add() example 3")
        print("----------------------------")
        for _ in range(100):
            case = list(set(random.randrange(1, 20000) for _ in range(900)))
            tree = AVL()
            for value in case:
                tree.add(value)
            if not tree.is_valid_avl():
                raise Exception("PROBLEM WITH ADD OPERATION")
        print('add() stress test finished')

    def test_remove(self):
        print("\nPDF - method remove() example 1")
        print("-------------------------------")
        test_cases = (
            ((1, 2, 3), 1),  # no AVL rotation
            ((1, 2, 3), 2),  # no AVL rotation
            ((1, 2, 3), 3),  # no AVL rotation
            ((50, 40, 60, 30, 70, 20, 80, 45), 0),
            ((50, 40, 60, 30, 70, 20, 80, 45), 45),  # no AVL rotation
            ((50, 40, 60, 30, 70, 20, 80, 45), 40),  # no AVL rotation
            ((50, 40, 60, 30, 70, 20, 80, 45), 30),  # no AVL rotation
        )
        for case, del_value in test_cases:
            tree = AVL(case)
            print('INPUT  :', tree, "DEL:", del_value)
            tree.remove(del_value)
            print('RESULT :', tree)

        print(tree.is_valid_avl())


        print("\nPDF - method remove() example 2")
        print("-------------------------------")
        test_cases = (
            ((50, 40, 60, 30, 70, 20, 80, 45), 20),  # RR
            ((50, 40, 60, 30, 70, 20, 80, 15), 40),  # LL
            ((50, 40, 60, 30, 70, 20, 80, 35), 20),  # RL
            ((50, 40, 60, 30, 70, 20, 80, 25), 40),  # LR
        )
        for case, del_value in test_cases:
            tree = AVL(case)
            print('INPUT  :', tree, "DEL:", del_value)
            tree.remove(del_value)
            print('RESULT :', tree)

        print(tree.is_valid_avl())

        print("\nPDF - method remove() example 3")
        print("-------------------------------")
        case = range(-9, 16, 2)
        tree = AVL(case)
        for del_value in case:
            print('INPUT  :', tree, del_value)
            tree.remove(del_value)
            print('RESULT :', tree)
            print(tree.is_valid_avl())

        print("\nPDF - method remove() example 4")
        print("-------------------------------")
        case = range(0, 34, 3)
        tree = AVL(case)
        for _ in case[:-2]:
            root_value = tree.get_root().value
            print('INPUT  :', tree, root_value)
            tree.remove(root_value)
            print('RESULT :', tree)
            print(tree.is_valid_avl())

        print("\nPDF - method remove() example 5")
        print("-------------------------------")
        for _ in range(100):
            case = list(set(random.randrange(1, 20000) for _ in range(900)))
            tree = AVL(case)
            for value in case[::2]:
                tree.remove(value)
            if not tree.is_valid_avl():
                raise Exception("PROBLEM WITH REMOVE OPERATION")
        print('remove() stress test finished')


        case = [8, 15, 11, 12, 3, 16, 9, 5, 13, 2, 17, 10, 14, 18, 1, 19, 4, 6, 7, 20]
        tree = AVL(case)
        tree.remove(8)
        print(tree.is_valid_avl())
        tree.remove(11)
        print(tree.is_valid_avl())


if __name__ == '__main__':
    unittest.main()
