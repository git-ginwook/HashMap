# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Stack ADT - Linked Nodes Implementation
# Due Date: 5/2/2022
# Description: implement stack ADT using Linked Nodes that can perform:
#   1) push(): add a new node to the top of the stack
#   2) pop(): remove the head node from the stack and return the top value
#   3) top(): return the value from the head node without removing it


from SLNode import SLNode


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self) -> None:
        """
        Initialize new stack with head node
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'STACK ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        add a new node with 'value' to the top of the stack
        """
        # create a new node
        node = SLNode(value, self._head)

        # switch the head node to the new node
        self._head = node

    def pop(self) -> object:
        """
        remove the head node from the stack

        return the top value

        exception case:
        - the stack is empty; nothing to pop
        """
        # exception case
        if self.is_empty():
            raise StackException

        # store the value of the top of the stack
        val = self._head.value

        # remove the top of the stack
        self._head = self._head.next

        # return the stored value
        return val

    def top(self) -> object:
        """
        return the head value of the stack (without removing it)

        exception case:
        - the stack is empty; nothing to return
        """
        # exception case
        if self.is_empty():
            raise StackException

        # return the top value of the stack
        return self._head.value

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)