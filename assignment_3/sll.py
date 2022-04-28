# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Singly Linked List Implementation
# Due Date: 5/2/2022
# Description: implement singly LinkedList object that can perform:
#   1) insert_front(): add a new node at the beginning the linked list
#   2) insert_back(): add a new node at the end of the linked list
#   3) insert_at_index(): add a new node at the specified index position
#   4) remove_at_index(): remove node at the specified index position
#   5) remove(): remove a specified value from the linked list
#   6) count(): add up the number of a specified value in the linked list
#   7) find(): check whether a specified value exists in the linked list
#   8) slice(): copy a specified portion of the linked list to a new one list


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
        """
        # initialize 'node' object variable
        node = self._head

        # move to the end of the linked list
        for _ in range(self.length()):
            node = node.next

        # add a new node after the current end node
        node.next = SLNode(value)

    def insert_at_index(self, index: int, value: object) -> None:
        """
        add a new node at the specified 'index' position
        connect the immediately following node as 'next' of the new node

        exception case:
        - invalid index raises SLLException
        """
        # exception case
        if index < 0 or index > self.length():
            raise SLLException

        # initialize 'node' object variable
        node = self._head

        # move to the one node before the specified 'index' position
        for _ in range(index):
            node = node.next

        # insert a new node at the specified 'index' position
        post = node.next
        node.next = SLNode(value, post)

    def remove_at_index(self, index: int) -> None:
        """
        remove the node at the specified 'index' position
        skip the target node when linking node(s)

        exception case:
        - invalid index raises SLLException
        base case:
        - empty linked list; nothing to remove
        """
        # exception case
        if index < 0 or index > (self.length()-1):
            raise SLLException

        # base case
        if self.length() == 0:
            return

        # initialize 'curr' and 'prev' nodes
        curr = self._head.next
        prev = self._head

        # move to the specified 'index' position
        for _ in range(index):
            prev = curr
            curr = curr.next

        # skip 'curr' node at 'index' position
        prev.next = curr.next

    def remove(self, value: object) -> bool:
        """
        find and remove 'value' in the singly linked list

        return True, if 'value' to be removed is found
        return False, if 'value' to be removed is not found

        base case:
        - empty list; nothing can be removed  -> return False
        """
        # base case
        if self.length() == 0:
            return False

        # initialize 'curr' object variable
        curr = self._head

        # traverse the list from the beginning to the end looking for 'value'
        for _ in range(self.length()):
            prev = curr
            curr = curr.next

            # when 'value' is found, remove 'value'
            if curr.value == value:
                prev.next = curr.next
                return True

        # nothing matches with 'value'
        return False

    def count(self, value: object) -> int:
        """
        sum up the number of 'value' in the singly linked list

        return the number of 'value'
        """
        # set initial 'count' variable
        count = 0

        # point to the first node after FrontSentinel
        curr = self._head.next

        # traverse the list from the beginning to the end looking for 'value'
        for _ in range(self.length()):
            # increment count when 'value' is found
            if curr.value == value:
                count += 1

            # move to the next node
            curr = curr.next

        return count

    def find(self, value: object) -> bool:
        """
        check whether 'value' exists in the singly linked list

        return True, if 'value' is found
        return False, if 'value' is not found
        """
        # point to the first node after FrontSentinel
        curr = self._head.next

        # traverse the list from the beginning to the end looking for 'value'
        for _ in range(self.length()):
            # return True when 'value' is found
            if curr.value == value:
                return True

            # move to the next node
            curr = curr.next

        # nothing matches with 'value'
        return False

    def slice(self, start_index: int, size: int) -> "LinkedList":
        """
        copy the requested number (='size') of nodes from 'start_index'
        paste all to a new, empty LinkedList object

        return a new LinkedList with the requested slice

        exception case:
        (1) invalid 'start_index' raises SLLException
        (2) invalid 'size' raises SLLException
        """
        # exception case
        if start_index < 0 or start_index > (self.length()-1):
            raise SLLException                  # (1)
        if size < 0 or size > (self.length() - start_index):
            raise SLLException                  # (2)

        # point to the first node after FrontSentinel
        curr = self._head.next

        # move to the 'start_index' position
        for _ in range(start_index):
            curr = curr.next

        # create a new LinkedList object
        new_lst = LinkedList()

        # slice the requested 'size' and paste to 'new_lst'
        for pos in range(size):
            new_lst.insert_back(curr.value)
            curr = curr.next

        return new_lst


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
