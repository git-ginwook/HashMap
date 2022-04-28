# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Singly Linked List Implementation
# Due Date: 5/2/2022
# Description:


from SLNode import *


class SLLException(Exception):
    """
    Custom exception class to be used by Singly Linked List
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class LinkedList:
    def __init__(self, start_list=None) -> None:
        """
        Initialize new linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = SLNode(None)

        # populate SLL with initial values (if provided)
        # before using this feature, implement insert_back() method
        if start_list is not None:
            for value in start_list:
                self.insert_back(value)

    def __str__(self) -> str:
        """
        Return content of singly linked list in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'SLL ['
        node = self._head.next
        while node:
            out += str(node.value)
            if node.next:
                out += ' -> '
            node = node.next
        out += ']'
        return out

    def length(self) -> int:
        """
        Return the length of the linked list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        length = 0
        node = self._head.next
        while node:
            length += 1
            node = node.next
        return length

    def is_empty(self) -> bool:
        """
        Return True is list is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return not self._head.next

    # ------------------------------------------------------------------ #

    def insert_front(self, value: object) -> None:
        """
        add a new SLNode at the beginning of the singly linked list
        """
        # store the first SLNode, if any
        post = self._head.next

        # insert a new SLNode at the front (after FrontSentinel)
        self._head.next = SLNode(value, post)

    def insert_back(self, value: object) -> None:
        """
        add a new SLNode at the end of the singly linked list

        base case:
        - linked list is empty: add a new node right after FrontSentinel
        """
        # base case
        if self._head.next is None:
            self._head.next = SLNode(value)
            return

        # point to the first node after FrontSentinel
        node = self._head.next

        # move to the end of the linked list
        for _ in range(self.length()-1):
            node = node.next

        # add a new node after the current end node
        node.next = SLNode(value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        add a new node at the specified 'index' position
        connect the immediately following node as 'next' of the new node

        exception case:
        - invalid index raises SLLException
        base case:
        - insert 'value' at zero 'index' (=insert_front())
        """
        # exception case
        if index < 0 or index > self.length():
            raise SLLException

        # base case
        if index == 0:
            self.insert_front(value)
            return

        # point to the first node after FrontSentinel
        node = self._head.next

        # move to the one node before the specified 'index' position
        for _ in range(index-1):
            node = node.next

        # insert a new node at the specified 'index' position
        post = node.next
        node.next = SLNode(value, post)

    def remove_at_index(self, index: int) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def remove(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        pass

    def count(self, value: object) -> int:
        """
        TODO: Write this implementation
        """
        pass

    def find(self, value: object) -> bool:
        """
        TODO: Write this implementation
        """
        pass

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        TODO: Write this implementation
        """
        pass


if __name__ == '__main__':

    print('\n# insert_front example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_front('A')
    lst.insert_front('B')
    lst.insert_front('C')
    print(lst)

    print('\n# insert_back example 1')
    lst = LinkedList()
    print(lst)
    lst.insert_back('C')
    lst.insert_back('B')
    lst.insert_back('A')
    print(lst)

    print('\n# insert_at_index example 1')
    lst = LinkedList()
    test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F')]
    for index, value in test_cases:
        print('Insert of', value, 'at', index, ': ', end='')
        try:
            lst.insert_at_index(index, value)
            print(lst)
        except Exception as e:
            print(type(e))

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

    print('\n# count example 1')
    lst = LinkedList([1, 2, 3, 1, 2, 2])
    print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

    print('\n# find example 1')
    lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
    print(lst)
    print(lst.find("Waldo"))
    print(lst.find("Superman"))
    print(lst.find("Santa Clause"))

    print('\n# slice example 1')
    lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll_slice = lst.slice(1, 3)
    print(lst, ll_slice, sep="\n")
    ll_slice.remove_at_index(0)
    print(lst, ll_slice, sep="\n")

    print('\n# slice example 2')
    lst = LinkedList([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", lst)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1)]
    for index, size in slices:
        print("Slice", index, "/", size, end="")
        try:
            print(" --- OK: ", lst.slice(index, size))
        except:
            print(" --- exception occurred.")
