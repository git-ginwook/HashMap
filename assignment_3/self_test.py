import unittest
from sll import *
from stack_da import *
from queue_sa import *


class TestAssignment(unittest.TestCase):
    # part 1 - singly linked list
    def test_insert_front_back(self):
        print('\n# insert_front example 1')
        lst = LinkedList()
        print(lst)
        lst.insert_front('A')
        lst.insert_front('B')
        lst.insert_front('C')
        print(lst)

        print(lst.length())

        print('\n# insert_back example 1')
        lst = LinkedList()
        print(lst)
        lst.insert_back('C')
        lst.insert_back('B')
        lst.insert_back('A')
        # lst.insert_back('A')
        # lst.insert_back('A')
        print(lst)

    def test_insert_at_index(self):
        print('\n# insert_at_index example 1')
        lst = LinkedList()
        test_cases = [(0, 'A'), (0, 'B'), (1, 'C'), (3, 'D'), (-1, 'E'), (5, 'F'),
                      (1, 'X')]
        for index, value in test_cases:
            print('Insert of', value, 'at', index, ': ', end='')
            try:
                lst.insert_at_index(index, value)
                print(lst)
            except Exception as e:
                print(type(e))

        lst = LinkedList([1, 2, 3])
        try:
            lst.insert_at_index(2, "B")
            lst.insert_at_index(3, "A")
            print(lst)
        except:
            print("exception")

    def test_remove_at_index(self):
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

        # remove the last node
        lst = LinkedList([1, 2, 3, 4, 5, 6])
        lst.remove_at_index(5)
        print(lst)

    def test_remove(self):
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

    def test_count(self):
        print('\n# count example 1')
        lst = LinkedList([1, 2, 3, 1, 2, 2, 1])
        print(lst, lst.count(1), lst.count(2), lst.count(3), lst.count(4))

        lst = LinkedList()
        print(lst, lst.count(2))

        lst = LinkedList([1])
        print(lst, lst.count(2), lst.count(1))

    def test_find(self):
        print('\n# find example 1')
        lst = LinkedList(["Waldo", "Clark Kent", "Homer", "Santa Clause"])
        print(lst)
        print(lst.find("Waldo"))
        print(lst.find("Superman"))
        print(lst.find("Santa Clause"))

        print(lst.find("Homer"))
        print(lst.find("Clark Kent"))

    def test_slice(self):
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

        # test slicing an empty linked list
        lst = LinkedList()
        try:
            print(lst.slice(0, 0))
        except:
            print("-- exception")

    # part 2 stack ADT - dynamic array implementation
    def test_push(self):
        print("\n# push example 1")
        s = Stack()
        print(s)
        for value in [1, 2, 3, 4, 5, 1, 2]:
            s.push(value)
        print(s)

    def test_pop(self):
        print("\n# pop example 1")
        s = Stack()
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))
        for value in [1, 2, 3, 4, 5, "A", 5]:
            s.push(value)
        for i in range(8):
            try:
                print(s.pop())
            except Exception as e:
                print("Exception:", type(e))

    def test_top(self):
        print("\n# top example 1")
        s = Stack()
        try:
            s.top()
        except Exception as e:
            print("No elements in stack", type(e))
        s.push(10)
        s.push(20)
        s.push(30)
        s.push("A")
        print(s)
        print(s.top())
        print(s.top())
        print(s)

    # part 3 Queue ADT - static array implementation
    def test_enqueue(self):
        print("\n# enqueue example 1")
        q = Queue()
        print(q)
        for value in [1, 2, 3, 4, 5]:
            q.enqueue(value)
        print(q)

        # test after dequeue


if __name__ == '__main__':
    unittest.main()
