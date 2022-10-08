# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 4 - Binary Search Tree Implementation
# Due Date: 5/17/2022
# Description: implement Binary Search Tree that can perform:
#   1) add(): insert a new value to the tree (duplicates are allowed)
#   2) remove(): remove a target value from the tree
#   3) contains(): check whether a target value is in the tree
#   4) inorder_traversal(): traverse values in inorder (left - visit - right)
#   5) find_min(): identify the lowest value in the tree
#   6) find_max(): identify the highest value in the tree
#   7) is_empty(): check whether the tree is empty
#   8) make_empty(): reset the tree to contain nothing

import random
from queue_and_stack import Queue, Stack


class BSTNode:
    """
    Binary Search Tree Node class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """

    def __init__(self, value: object) -> None:
        """
        Initialize a new BST node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.value = value   # to store node's data
        self.left = None     # pointer to root of left subtree
        self.right = None    # pointer to root of right subtree

    def __str__(self) -> str:
        """
        Override string method
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'BST Node: {}'.format(self.value)


class BST:
    """
    Binary Search Tree class
    """

    def __init__(self, start_tree=None) -> None:
        """
        Initialize new Binary Search Tree
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._root = None

        # populate BST with initial values (if provided)
        # before using this feature, implement add() method
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of BST in human-readable form using pre-order traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        values = []
        self._str_helper(self._root, values)
        return "BST pre-order { " + ", ".join(values) + " }"

    def _str_helper(self, node: BSTNode, values: []) -> None:
        """
        Helper method for __str__. Does pre-order tree traversal
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if not node:
            return
        values.append(str(node.value))
        self._str_helper(node.left, values)
        self._str_helper(node.right, values)

    def get_root(self) -> BSTNode:
        """
        Return root of tree, or None if empty
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._root

    def is_valid_bst(self) -> bool:
        """
        Perform pre-order traversal of the tree.
        Return False if nodes don't adhere to the bst ordering property.
        This is intended to be a troubleshooting 'helper' method to help
        find any inconsistencies in the tree after the add() or remove()
        operations. Review the code to understand what this method is
        checking and how it determines whether the BST tree is correct.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        stack = Stack()
        stack.push(self._root)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                if node.left and node.left.value >= node.value:
                    return False
                if node.right and node.right.value < node.value:
                    return False
                stack.push(node.right)
                stack.push(node.left)
        return True

    # ------------------------------------------------------------------ #

    def add(self, value: object) -> None:
        """
        add a new node with 'value' to the tree

        a smaller value is added to the left subtree,
        a bigger or equal value is added to the right subtree

        base case:
        - empty tree
        """
        # base case
        if self._root is None:
            self._root = BSTNode(value)
            return

        # initialize a traversing node
        nd_parent = None
        nd_curr = self._root

        # iterate through the tree to find the insert position
        while nd_curr is not None:
            # parent node chasing the current node
            nd_parent = nd_curr

            # traverse to the left
            if value < nd_curr.value:
                nd_curr = nd_curr.left
            # traverse to the right
            else:
                nd_curr = nd_curr.right

        # add the value as the left leaf
        if value < nd_parent.value:
            nd_parent.left = BSTNode(value)
        # add the value as the right leaf
        else:
            nd_parent.right = BSTNode(value)

    def remove(self, value: object) -> bool:
        """
        remove a node with 'value' from the tree

        if there are duplicates of 'value',
        then remove the first one, closer to the root

        if the value is removed, return True
        otherwise, return False

        scenarios:
        (1) the target node has no subtrees
        (2) the target node has two subtrees
        (3) the target node has one subtree

        base case:
        - empty tree; nothing to remove
        """
        # base case
        if self._root is None:
            return False

        # initialize variables
        nd_parent = None
        nd_curr = self._root

        # find the target value
        while value != nd_curr.value:
            # parent node chasing the current node
            nd_parent = nd_curr

            # traverse left
            if value < nd_curr.value:
                nd_curr = nd_curr.left
            # traverse right
            else:
                nd_curr = nd_curr.right

            # target node not found
            if nd_curr is None:
                return False

        # scenario 1
        if nd_curr.left is None and nd_curr.right is None:
            self._remove_no_sub(nd_parent, nd_curr)
            return True

        # scenario 2
        elif nd_curr.left is not None and nd_curr.right is not None:
            self._remove_two_sub(nd_parent, nd_curr)
            return True

        # scenario 3
        else:
            self._remove_one_sub(nd_parent, nd_curr)
            return True

    def _remove_no_sub(self, parent: BSTNode, node: BSTNode) -> None:
        """
        remove 'node' that has no subtrees (neither left nor right nodes)

        base case:
        - target is the root
        """
        # base case
        if parent is None:
            self._root = None
            return

        # when the target node is in the left subtree of the parent
        if node.value < parent.value:
            parent.left = None

        # when the target node is in the right subtree of the parent
        else:
            parent.right = None

    def _remove_two_sub(self, parent: BSTNode, node: BSTNode) -> None:
        """
        remove 'node' that has two subtrees

        base case:
        - target is the root
        """
        # initialize variables for inorder successor and its parent node
        par_suc = node
        in_suc = par_suc.right

        # pinpoint inorder successor and its parent
        while in_suc.left is not None:
            par_suc = in_suc
            in_suc = par_suc.left

        # rewiring nodes
        in_suc.left = node.left
        if node.right.value != in_suc.value:
            par_suc.left = in_suc.right
            in_suc.right = node.right

        # base case
        if parent is None:
            self._root = in_suc
            in_suc.parent = None
            return

        # when the target node was in the left subtree of its parent
        if node.value < parent.value:
            parent.left = in_suc

        # when the target node was in the right subtree of its parent
        else:
            parent.right = in_suc

    def _remove_one_sub(self, parent: BSTNode, node: BSTNode) -> None:
        """
        remove 'node' that has a left or right subtree (only)

        base case:
        - target is the root
        """
        # base case
        if parent is None:
            if node.left is not None:
                self._root = node.left
            else:
                self._root = node.right
            self._root.parent = None
            return

        # when the target node is in the left subtree of the parent
        if node.value < parent.value:
            if node.left is not None:
                parent.left = node.left
            else:
                parent.left = node.right

        # when the target node is in the right subtree of the parent
        else:
            if node.left is not None:
                parent.right = node.left
            else:
                parent.right = node.right

    def contains(self, value: object) -> bool:
        """
        search for 'value' in the tree

        if the value is found, return True
        otherwise, return False

        base case:
        - empty tree; contains nothing
        """
        # base case
        if self._root is None:
            return False

        # initialize a node variable
        nd_curr = self._root

        # find the target value
        while value != nd_curr.value:
            # traverse left
            if value < nd_curr.value:
                nd_curr = nd_curr.left
            # traverse right
            elif value > nd_curr.value:
                nd_curr = nd_curr.right

            # target value not found
            if nd_curr is None:
                return False

        # target value found
        return True

    def inorder_traversal(self) -> Queue:
        """
        perform an *inorder traversal* of the tree
            * traverse left -> visit -> traverse right

        return a Queue object with the values in inorder

        base case:
        - empty tree; return an empty Queue
        """
        # create an empty queue
        queue = Queue()

        # base case
        if self._root is None:
            return queue

        # initialize a node
        node = self._root

        # use a recursive helper method to build the queue object
        return self._inorder(node, queue)

    def _inorder(self, node: BSTNode, queue: Queue) -> Queue:
        """
        a recursive helper method to enqueue all values in the tree in inorder

        return the fully-built Queue object
        """
        if node is not None:
            self._inorder(node.left, queue)
            queue.enqueue(node.value)
            self._inorder(node.right, queue)

        return queue

    def find_min(self) -> object:
        """
        identify the lowest value in the tree

        base case:
        - empty tree; no minimum value -> None
        """
        # base case
        if self._root is None:
            return None

        # initialize a traversing node
        node = self._root

        # traverse the tree far down the left
        while node is not None:
            parent = node
            node = node.left

        # return the lowest value
        return parent.value

    def find_max(self) -> object:
        """
        identify the highest value in the tree

        base case:
        - empty tree; no maximum value -> None
        """
        # base case
        if self._root is None:
            return None

        # initialize a traversing node
        node = self._root

        # traverse the tree far down the right
        while node is not None:
            parent = node
            node = node.right

        # return the highest value
        return parent.value

    def is_empty(self) -> bool:
        """
        check whether the tree is empty

        if the root is None, return True
        Otherwise, return False
        """
        # check the root
        if self._root is None:
            return True

        return False

    def make_empty(self) -> None:
        """
        reset the tree; contains nothing
        """
        self._root = None


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == '__main__':

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
        (30, 20, 10, 1, 5),
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

    print("\nPDF - method inorder_traversal() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree.inorder_traversal())

    print("\nPDF - method inorder_traversal() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree.inorder_traversal())

    print("\nPDF - method find_min() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_min() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Minimum value is:", tree.find_min())

    print("\nPDF - method find_max() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method find_max() example 2")
    print("---------------------------------")
    tree = BST([8, 10, -4, 5, -1])
    print(tree)
    print("Maximum value is:", tree.find_max())

    print("\nPDF - method is_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method is_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree is empty:", tree.is_empty())

    print("\nPDF - method make_empty() example 1")
    print("---------------------------------")
    tree = BST([10, 20, 5, 15, 17, 7, 12])
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)

    print("\nPDF - method make_empty() example 2")
    print("---------------------------------")
    tree = BST()
    print("Tree before make_empty():", tree)
    tree.make_empty()
    print("Tree after make_empty(): ", tree)
