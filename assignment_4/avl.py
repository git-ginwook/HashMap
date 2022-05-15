# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 - AVL Implementation
# Due Date: 5/17/2022
# Description:


import random
from queue_and_stack import Queue, Stack
from bst import BSTNode, BST


class AVLNode(BSTNode):
    """
    AVL Tree Node class. Inherits from BSTNode
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    def __init__(self, value: object) -> None:
        """
        Initialize a new AVL node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(value)

        # new variables needed for AVL
        self.parent = None
        self.height = 0

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'AVL Node: {}'.format(self.value)


class AVL(BST):
    """
    AVL Tree class. Inherits from BST
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize a new AVL Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        # call __init__() from parent class
        super().__init__(start_tree)

    def __str__(self) -> str:
        """
        Return content of AVL in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        super()._str_helper(self._root, values)
        return "AVL pre-order { " + ", ".join(values) + " }"

    def is_valid_avl(self) -> bool:
        """
        Perform pre-order traversal of the tree. Return False if there
        are any problems with attributes of any of the nodes in the tree.

        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the AVL tree is correct.

        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                # check for correct height (relative to children)
                left = node.left.height if node.left else -1
                right = node.right.height if node.right else -1
                if node.height != 1 + max(left, right):
                    return False

                if node.parent:
                    # parent and child pointers are in sync
                    if node.value < node.parent.value:
                        check_node = node.parent.left
                    else:
                        check_node = node.parent.right
                    if check_node != node:
                        return False
                else:
                    # NULL parent is only allowed on the root of the tree
                    if node != self._root:
                        return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        TODO: Write your implementation
        insert a new node...
        rebalance...

        base case:
        - empty tree
        """
        # base case
        if self._root is None:
            self._root = AVLNode(value)
            return

        # initialize a traversing node
        node = self._root
        p_node = node.parent

        # iterate through the tree to find the correct position
        while node is not None:
            # no duplicates are allowed
            if value == node.value:
                return

            # parent node chasing the current node
            p_node = node

            if value < node.value:
                node = node.left                # traverse left
            else:
                node = node.right               # traverse right

        # add a new node
        if value < p_node.value:
            p_node.left = AVLNode(value)        # add on the left subtree
            node = p_node.left

        else:
            p_node.right = AVLNode(value)       # add on the right subtree
            node = p_node.right

        # update node's parent
        node.parent = p_node

        # trace upward and rebalance along the way
        while p_node is not None:
            self._rebalance(p_node)
            p_node = p_node.parent

    def remove(self, value: object) -> bool:
        """
        TODO: Write your implementation
        """
        pass

    # Experiment and see if you can use the optional                         #
    # subtree removal methods defined in the BST here in the AVL.            #
    # Call normally using self -> self._remove_no_subtrees(parent, node)     #
    # You need to override the _remove_two_subtrees method in any case.      #
    # Remove these comments.                                                 #
    # Remove these method stubs if you decide not to use them.               #

    def _remove_two_subtrees(self, parent: AVLNode, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        pass

    # It's highly recommended to implement                          #
    # the following methods for balancing the AVL Tree.             #
    # Remove these comments.                                        #
    # Remove these method stubs if you decide not to use them.      #
    # Change these methods in any way you'd like.                   #

    def _balance_factor(self, node: AVLNode) -> int:
        """
        TODO: Write your implementation
        """
        return self._get_height(node.right) - self._get_height(node.left)

    def _get_height(self, node: AVLNode) -> int:
        """
        TODO: Write your implementation
        """
        # height of an empty subtree
        if node is None:
            return -1

        return node.height

    def _rotate_left(self, node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        # create a pointer for the upcoming subtree root after rotation
        center = node.right

        # attach center node's left subtree to the node's right
        node.right = center.left
        if node.right is not None:
            node.right.parent = node

        # update affected node's properties
        center.left = node
        # node.parent = center

        # update heights
        self._update_height(node)
        self._update_height(center)

        return center

    def _rotate_right(self, node: AVLNode) -> AVLNode:
        """
        TODO: Write your implementation
        """
        # create a pointer for the upcoming subtree root after rotation
        center = node.left

        # attach center node's right subtree to the node's left
        node.left = center.right
        if node.left is not None:
            node.left.parent = node

        # update affected node's properties
        center.right = node
        # node.parent = center

        # update heights
        self._update_height(node)
        self._update_height(center)

        return center

    def _update_height(self, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        """
        # heights of left and right subtrees
        h_left = self._get_height(node.left)
        h_right = self._get_height(node.right)

        # update node's height
        node.height = max(h_left, h_right) + 1

    def _rebalance(self, node: AVLNode) -> None:
        """
        TODO: Write your implementation
        base case:
        - balanced node; update height
        """
        # base case
        if -1 <= self._balance_factor(node) <= 1:
            self._update_height(node)
            return

        # check height balance (left-heavy)
        if self._balance_factor(node) < -1:
            # check for double rotation
            if self._balance_factor(node.left) > 0:
                new_center = self._rotate_left(node.left)
                node.left.parent = new_center
                node.left = new_center
                new_center.parent = node

            # single rotation (right)
            sub_root = self._rotate_right(node)

        # check height balance (right-heavy)
        else:
            # check for double rotation
            if self._balance_factor(node.right) < 0:
                new_center = self._rotate_right(node.right)
                node.right.parent = new_center
                node.right = new_center
                new_center.parent = node

            # single rotation (left)
            sub_root = self._rotate_left(node)

        # update sub_root's parent
        sub_root.parent = node.parent

        # update sub_root's position relative to its parent
        if node.parent is not None:
            if sub_root.value < node.parent.value:
                node.parent.left = sub_root
            else:
                node.parent.right = sub_root

            node.parent = sub_root

        else:
            node.parent = sub_root
            self._root = sub_root


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

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
        (10, 20, 30, 40, 50),   # RR, RR
        (10, 20, 30, 50, 40),   # RR, RL
        (30, 20, 10, 5, 1),     # LL, LL
        (30, 20, 10, 1, 5),     # LL, LR
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

    print("\nPDF - method remove() example 3")
    print("-------------------------------")
    case = range(-9, 16, 2)
    tree = AVL(case)
    for del_value in case:
        print('INPUT  :', tree, del_value)
        tree.remove(del_value)
        print('RESULT :', tree)

    print("\nPDF - method remove() example 4")
    print("-------------------------------")
    case = range(0, 34, 3)
    tree = AVL(case)
    for _ in case[:-2]:
        root_value = tree.get_root().value
        print('INPUT  :', tree, root_value)
        tree.remove(root_value)
        print('RESULT :', tree)

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

    print("\nPDF - method contains() example 1")
    print("---------------------------------")
    tree = AVL([10, 5, 15])
    print(tree.contains(15))
    print(tree.contains(-10))
    print(tree.contains(15))

    print("\nPDF - method contains() example 2")
    print("---------------------------------")
    tree = AVL()
    print(tree.contains(0))

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = AVL([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = AVL([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = AVL()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
