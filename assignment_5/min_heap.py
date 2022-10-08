# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5 - MinHeap Implementation
# Due Date: 5/23/2022
# Description: implement Min Heap that can perform:
#   1) add(): add a new object to the heap
#   2) is_empty(): check whether the heap is empty
#   3) get_min(): return the object at the root
#   4) remove_min(): return and remove the object at the root
#   5) build_heap(): overwrite a heap based on a new Dynamic Array
#   6) size(): count the number of items in the heap
#   7) clear(): empty the heap
#
#   standalone function and a helper method outside the MinHeap class
#   heapsort(): sort a Dynamic Array in non-ascending order using the Heapsort
#   _percolate_down(): move down until no children is greater than the element


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
        remove an object with the minimum key

        return the object

        exception case:
        - empty heap; nothing to remove

        base case:
        - single value in the heap
        """
        # exception case
        if self.is_empty():
            raise MinHeapException

        # store the minimum value to return
        min_val = self.get_min()

        # base case
        if self._heap.length() == 1:
            # remove the only value
            self._heap.remove_at_index(0)
            return min_val

        # index of the last element
        i_last = self._heap.length() - 1

        # copy the last element to the front
        val_last = self._heap.get_at_index(i_last)
        self._heap.set_at_index(0, val_last)

        # remove the last element
        self._heap.remove_at_index(i_last)

        # percolate down from the beginning
        _percolate_down(self._heap, 0, self._heap.length())

        return min_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        overwrite the heap with 'da' and reorder to maintain the heap property
        """
        # create a new dynamic array
        new_da = DynamicArray()

        # copy values in da to new_da
        for pos in range(da.length()):
            new_da.append(da.get_at_index(pos))

        # overwrite the current heap
        self._heap = new_da

        # find index of the first non-leaf
        non_leaf = da.length() // 2 - 1

        # percolation loop
        while non_leaf > -1:
            # percolate down
            _percolate_down(self._heap, non_leaf, da.length())
            # decrement non_leaf
            non_leaf -= 1

    def size(self) -> int:
        """
        return number of items in the heap that maintains the heap property

        """
        return self._heap.length()

    def clear(self) -> None:
        """
        clear the heap
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    sort 'da' in non-ascending order

    base case:
    - only one element; no further sort needed
    """
    # base case
    if da.length() == 1:
        return

    # build a heap out of 'da'
    hs = MinHeap()
    hs.build_heap(da)

    # reorder 'da'
    for pos in range(da.length()):
        val = hs.remove_min()
        da.set_at_index(pos, val)

    # create a counter variable
    k = da.length() - 1

    # percolating till k reaches the front of the array
    while k > 0:
        # get the min and the 'k'th values
        m_val = da.get_at_index(0)
        k_val = da.get_at_index(k)

        # swap the min and the 'k'th
        da.set_at_index(0, k_val)
        da.set_at_index(k, m_val)

        # percolate down
        _percolate_down(da, 0, k)

        # decrement k
        k -= 1


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int, count: int) -> None:
    """
    move the element down the heap until:
    either no children is smaller than it or it reached the bottom

    scenarios:
    (1) no child: nothing to percolate -> stop percolation
    (2) two children:
        (2-1) parent is greater than at least one of its children
        (2-2) both children are greater than parent -> stop percolation

    (3) only child:
        (3-1) left child is greater than parent
        (3-2) right child is greater than parent
        (3-3) the only child is greater than parent -> stop percolation
    """
    # percolate down while parent is within the heap boundary
    while parent < count:
        # update indices of left and right children
        left = 2 * parent + 1
        right = 2 * parent + 2

        # fetch values
        parent_val = da.get_at_index(parent)
        left_val = da.get_at_index(left) if left < count else None
        right_val = da.get_at_index(right) if right < count else None

        # scenario(1): no child
        if left_val is None and right_val is None:
            return

        # scenario(2): two children
        elif left_val is not None and right_val is not None:
            # scenario(2-1)
            if parent_val > left_val or parent_val > right_val:
                # update path by comparing left and right
                path = -1 if left_val <= right_val else 1

            # scenario(2-2)
            else:
                return

        # scenario(3): only child
        else:
            # scenario(3-1)
            if left_val is not None and parent_val > left_val:
                path = -1
            # scenario(3-2)
            elif right_val is not None and parent_val > right_val:
                path = 1
            # scenario(3-3)
            else:
                return

        # percolate down based on path value
        if path < 0:
            # swap with left
            da.set_at_index(parent, left_val)
            da.set_at_index(left, parent_val)
            # update parent index
            parent = left

        else:
            # swap with right
            da.set_at_index(parent, right_val)
            da.set_at_index(right, parent_val)
            # update parent index
            parent = right

    return

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
