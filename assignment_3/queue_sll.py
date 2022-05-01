# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Queue ADT - Linked Nodes Implementation
# Due Date: 5/2/2022
# Description: implement queue ADT using Linked Nodes that can perform:
#   1) enqueue(): add a new node to the end of the queue
#   2) dequeue(): remove the current 'head' node and return its value
#   3) front(): return the value of the 'head' node (without removing it)


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
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
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        append 'value' to the end of the queue

        base case:
        - if the queue is empty, the first node is both 'head' and 'tail'
        """
        # create a new node with 'value'
        node = SLNode(value)

        # base case
        if self.is_empty():
            self._head = node
            self._tail = node
            return

        # connect the new 'node' to the current 'tail'
        self._tail.next = node

        # reassign tail to the new 'node'
        self._tail = node

    def dequeue(self) -> object:
        """
        remove the 'head' node of the queue

        return the value of the original 'head' node

        exception case:
        - empty queue; nothing to remove
        """
        # exception case
        if self.is_empty():
            raise QueueException

        # store the current 'head' value
        val = self._head.value

        # switch 'head' node to the second node in the queue
        self._head = self._head.next

        # return the stored 'head' value
        return val

    def front(self) -> object:
        """
        return the 'head' value of the queue (without removing it)

        exception case:
        - empty queue; nothing to return
        """
        # exception case
        if self.is_empty():
            raise QueueException

        # return the current value of the 'head' node
        return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
