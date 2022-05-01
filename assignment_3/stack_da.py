# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Stack ADT - Dynamic Array Implementation
# Due Date: 5/2/2022
# Description: implement stack ADT using Dynamic Array that can perform:
#   1) push(): add a new element to the top of the stack
#   2) pop(): remove the top element from the stack and return the top value
#   3) top(): return the top value from the stack without removing it


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        """
        append a new 'value' to the top of the stack
        """
        # add 'value' to the top of the stack
        self._da.append(value)

    def pop(self) -> object:
        """
        remove the top element from the stack

        return the top value

        exception case:
        - the stack is empty; nothing to pop
        """
        # exception case
        if self.is_empty():
            raise StackException

        # store the value of the top of the stack
        top_idx = self.size() - 1
        val = self._da.get_at_index(top_idx)

        # remove the top of the stack
        self._da.remove_at_index(top_idx)

        # return the stored value
        return val

    def top(self) -> object:
        """
        return the top of the stack (without removing it)

        exception case:
        - the stack is empty; nothing to return
        """
        # exception case
        if self.is_empty():
            raise StackException

        return self._da.get_at_index(self.size() - 1)

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
