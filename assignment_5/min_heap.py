# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5 - MinHeap Implementation
# Due Date: 5/23/2022
# Description:


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """
        add 'node' adhering to the min heap property

        base case:
        - empty heap; add the first node
        """
        # base case
        if self.is_empty():
            self._heap.append(node)
            return

        # append a new node to the last open spot
        self._heap.append(node)

        # indices of the current node and its parent
        cn = self._heap.length() - 1
        pn = (cn - 1) // 2

        # compare values of the current and its parent
        while self._heap.get_at_index(cn) < self._heap.get_at_index(pn):
            # swap parent and current nodes
            temp_val = self._heap.get_at_index(cn)
            self._heap.set_at_index(cn, self._heap.get_at_index(pn))
            self._heap.set_at_index(pn, temp_val)

            # exit when reached the beginning
            if pn == 0:
                return

            # traverse up the heap
            cn = pn
            pn = (cn - 1) // 2

        return

    def is_empty(self) -> bool:
        """
        return True if the heap is empty
        return False otherwise
        """
        return self._heap.is_empty()

    def get_min(self) -> object:
        """
        return the minimum object

        exception case:
        - empty heap; no min to return
        """
        # exception case
        if self.is_empty():
            raise MinHeapException

        # return the min
        return self._heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        TODO: Write this implementation
        exception case:
        - empty heap; nothing to remove

        base case:
        - single value in the heap
        """
        # exception case
        if self.is_empty():
            raise MinHeapException

        # base case
        if self._heap.length() == 1:
            # store and remove the only value
            min_val = self.get_min()
            self._heap.remove_at_index(0)

            return min_val

        # store the minimum value to return
        min_val = self.get_min()

        # index of the last element
        i_last = self._heap.length() - 1

        # copy the last element to the front
        val_last = self._heap.get_at_index(i_last)
        self._heap.set_at_index(0, val_last)

        # remove the last element
        self._heap.remove_at_index(i_last)

        # initialize variables for left and right children
        cn = 0                                  # current node
        cn_l = 2 * 0 + 1                        # left children
        cn_r = 2 * 0 + 2                        # right children

        cn_val = self._heap.get_at_index(cn)
        cn_l_val = self._heap.get_at_index(cn_l)
        cn_r_val = self._heap.get_at_index(cn_r)

        # while the replaced node is within the heap boundary
        while cn < self._heap.length():
            # both none
            if cn_l_val is None and cn_r_val is None:
                return min_val

            # both children
            if cn_l_val is not None and cn_r_val is not None:
                # if left and right are equal
                if cn_l_val == cn_r_val:
                    if cn_val > cn_l_val:
                        # swap with left

                if cn_val > min(cn_l_val, cn_r_val):
                    # left is smaller, swap with left
                    if cn_l_val < cn_r_val:

                    # right is smaller, swap with right
                    else:


            # one of children
            else:
                if cn_l_val is not None:
                    if cn_val > cn_l_val:
                        # swap
                else:
                    if cn_val > cn_r_val:
                        # swap





        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        TODO: Write this implementation
        """
        pass

    def size(self) -> int:
        """
        TODO: Write this implementation
        """
        pass

    def clear(self) -> None:
        """
        TODO: Write this implementation
        """
        pass


def heapsort(da: DynamicArray) -> None:
    """
    TODO: Write this implementation
    """
    pass


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int) -> None:
    """
    TODO: Write your implementation
    """
    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
