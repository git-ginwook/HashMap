# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2 - Bag ADT Implementation Part 2
# Due Date: 4/25/2022
# Description: implement Bag ADT class that can perform the following:
#   1) add(): add a new value into the bag
#   2) remove(): remove the first value that matches a specified value
#   3) count(): identify the number of a specified element in the bag
#   4) clear(): reset the bag to an empty bag
#   5) equal(): compares the contents of two bags to determine whether equal
#   6) __iter__(): enable the bag to iterate itself (create index variable)
#   7) __next__(): return the next item in the bag (using index as a pointer)


from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        """
        append 'value' to the bag
        """
        # append 'value'
        self._da.append(value)

    def remove(self, value: object) -> bool:
        """
        remove one 'value' from the bag, if a match is found

        return True when there is a match
        return False when there is no match
        """
        # search for a match (the first match)
        for pos in range(self.size()):
            # return True after removing the first match
            if value == self._da.get_at_index(pos):
                self._da.remove_at_index(pos)
                return True

        # return False when there is no match
        return False

    def count(self, value: object) -> int:
        """
        sum up the number of 'value' in the bag

        return the total number of 'value'
        """
        # set initial 'count' variable
        count = 0

        # increment 'count' each time a match is found
        for pos in range(self.size()):
            if value == self._da.get_at_index(pos):
                count += 1

        return count

    def clear(self) -> None:
        """
        remove all contents in the bag
        """
        # reassign the bag with a new dynamic array
        self._da = DynamicArray()

    def equal(self, second_bag: "Bag") -> bool:
        """
        compare contents of the bag with 'second_bag'

        equal bags mean that two bags have:
        - the same elements
        - the same number of each element

        order of elements doesn't matter

        return True if equal. Otherwise, return False

        base case: compare size
        - two bags cannot be equal if sizes are different
        """
        # base case
        if self.size() != second_bag.size():
            return False

        # compare count of each value in the two bags
        for pos in range(self.size()):
            # identify a value to compare
            val = self._da.get_at_index(pos)

            # return False if count defers
            if self.count(val) != second_bag.count(val):
                return False

        # two bags are equal
        return True

    def __iter__(self):
        """
        set a tracker for iterator

        return the class itself
        """
        # initialize an index for iterator
        self._index = 0

        return self

    def __next__(self):
        """
        fetch a value in the dynamic array pointed at 'index'

        increment 'index' for the next iteration

        once 'index' reaches 'size' of the dynamic array,
        raise StopIteration

        return the fetched value
        """
        # fetch a value at 'index'
        try:
            val = self._da.get_at_index(self._index)
        # stop iteration when index is not less than 'size' of dynamic array
        except DynamicArrayException:
            raise StopIteration

        # increment 'index' for the next iteration
        self._index += 1

        return val

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
