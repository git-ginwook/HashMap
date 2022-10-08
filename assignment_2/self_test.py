import unittest
from bag_da import *
from dynamic_array import *


class TestAssignment(unittest.TestCase):
    # part 1 - dynamic_array
    def test_remove_at_index(self):
        # index out of range
        da = DynamicArray()
        da.resize(21)
        [da.append(10) for i in range(21)]
        self.assertEqual(da.length(), 21)

        # self._size * 2 == 10
        [da.remove_at_index(0) for i in range(17)]
        self.assertEqual(da.get_capacity(), 10)

        # capacity 16. remove until size 3. see if capacity set to 10.
        da = DynamicArray()
        da.resize(16)
        [da.append(100) for i in range(16)]
        [da.remove_at_index(0) for i in range(14)]
        self.assertEqual(da.get_capacity(), 10)

        # given example 1
        print("\n# remove_at_index - example 1")
        da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
        print(da)
        da.remove_at_index(0)
        print(da)
        da.remove_at_index(6)
        print(da)
        da.remove_at_index(2)
        print(da)

        # given example 2
        print("\n# remove_at_index - example 2")
        da = DynamicArray([1024])
        print(da)
        for i in range(17):
            da.insert_at_index(i, i)
        print(da.length(), da.get_capacity())
        for i in range(16, -1, -1):
            da.remove_at_index(0)
        print(da)

        # given example 3
        print("\n# remove_at_index - example 3")
        da = DynamicArray()
        print(da.length(), da.get_capacity())
        [da.append(1) for i in range(100)]  # step 1 - add 100 elements
        print(da.length(), da.get_capacity())
        [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
        print(da.length(), da.get_capacity())
        da.remove_at_index(0)  # step 3 - remove 1 element
        print(da.length(), da.get_capacity())
        da.remove_at_index(0)  # step 4 - remove 1 element
        print(da.length(), da.get_capacity())
        [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
        print(da.length(), da.get_capacity())
        da.remove_at_index(0)  # step 6 - remove 1 element
        print(da.length(), da.get_capacity())
        da.remove_at_index(0)  # step 7 - remove 1 element
        print(da.length(), da.get_capacity())

        for i in range(14):
            print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
            da.remove_at_index(0)
            print(" After remove_at_index(): ", da.length(), da.get_capacity())

        # given example 4
        print("\n# remove at index - example 4")
        da = DynamicArray([1, 2, 3, 4, 5])
        print(da)
        for _ in range(5):
            da.remove_at_index(0)
            print(da)

    # part 2 - bag_da
    def test_bag_add(self):
        print("\n# add example 1")
        bag = Bag()
        print(bag)
        values = [10, 20, 30, 10, 20, 30]
        for value in values:
            bag.add(value)
        print(bag)

    def test_bag_remove(self):
        print("\n# remove example 1")
        bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
        print(bag)
        print(bag.remove(7), bag)
        print(bag.remove(3), bag)
        print(bag.remove(3), bag)
        print(bag.remove(3), bag)
        print(bag.remove(3), bag)

    def test_bag_count(self):
        print("\n# count example 1")
        bag = Bag([1, 2, 3, 1, 2, 2])
        print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    def test_bag_clear(self):
        print("\n# clear example 1")
        bag = Bag([1, 2, 3, 1, 2, 3])
        print(bag)
        bag.clear()
        print(bag)

    def test_bag_equal(self):
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

    def test_bag_iternext(self):
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


if __name__ == '__main__':
    unittest.main()
