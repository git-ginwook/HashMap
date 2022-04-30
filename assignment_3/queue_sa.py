# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3 - Queue ADT - Static Array Implementation
# Due Date: 5/2/2022
# Description:


from static_array import StaticArray


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue based on Static Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._sa = StaticArray(4)
        self._front = 0
        self._back = -1
        self._current_size = 0

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        size = self._current_size
        out = "QUEUE: " + str(size) + " element(s). ["

        front_index = self._front
        for _ in range(size - 1):
            out += str(self._sa[front_index]) + ', '
            front_index = self._increment(front_index)

        if size > 0:
            out += str(self._sa[front_index])

        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size == 0

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._current_size

    def _increment(self, index: int) -> int:
        """
        Move index to next position
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """

        # employ wraparound if needed
        index += 1
        if index == self._sa.length():
            index = 0

        return index

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        """
        append 'value' to the end of the queue

        note:
        - 'capacity' means the size of the Static Array behind the queue ADT
        - 'size' means the number of elements in the queue
        """
        # double 'capacity' when 'size' and 'capacity' are equal
        if self._current_size == self._sa.length():
            self._double_queue()

        # increment 'back' position
        self._back = self._increment(self._back)

        # add 'value' to the 'back' of the queue
        self._sa.set(self._back, value)

        # increase 'size'
        self._current_size += 1

    def dequeue(self) -> object:
        """
        remove the value at the beginning of the queue

        return the value

        exception case:
        - empty queue; nothing to remove
        """
        # exception case
        if self.is_empty():
            raise QueueException

        # store 'front' value
        val = self._sa.get(self._front)

        # move 'front' position
        self._front = self._increment(self._front)

        # decrease 'size'
        self._current_size -= 1

        # reset if the queue is empty
        if self._current_size == 0:
            self._sa = StaticArray(4)           # adjust 'capacity'
            self._front = 0                     # reset 'front' position
            self._back = -1                     # reset 'back' position

        return val

    def front(self) -> object:
        """
        TODO: Write this implementation
        """
        pass

    # The method below is optional, but recommended, to implement. #
    # You may alter it in any way you see fit.                     #

    def _double_queue(self) -> None:
        """
        TODO: Write this implementation
        """
        capa = self._sa.length() * 2
        new_sa = StaticArray(capa)

        #
        start = self._front

        # reset 'front' and 'back'
        self._front = 0
        self._back = -1

        # reindex
        for pos in range(self._current_size):
            self._back = self._increment(self._back)

            val = self._sa.get(start)

            new_sa.set(self._back, val)

            start = self._increment(start)

        # switch to the new Static Array
        self._sa = new_sa


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
    for i in range(q.size() + 1):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))
    for value in [6, 7, 8, 111, 222, 3333, 4444]:
        q.enqueue(value)
    print(q)

    print('\n# front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
