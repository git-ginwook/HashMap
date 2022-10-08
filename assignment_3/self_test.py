import unittest
#from sll import *
from stack_da import *
# from queue_sa import *
from stack_sll import *
from queue_sll import *


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


    def test_dequeue_and_front(self):
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

        # dequeue and enqueue combo
        q.dequeue()
        q.enqueue("X")
        q.enqueue("Y")
        q.enqueue("Z")
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.enqueue("A")
        q.enqueue("B")
        q.enqueue("C")
        print(q)

        # reset empty queue
        q.dequeue()
        print(q.front())
        q.dequeue()
        print(q.front())
        q.dequeue()
        print(q.front())
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        q.dequeue()
        print(q)

        # test empty front()
        try:
            print(q.front())
        except Exception as ex:
            print("no element in the front", type(ex))

    # part 4 Stack ADT - Linked Nodes Implementation
    def test_push_4(self):
        print("\n# push example 1")
        s = Stack()
        print(s)
        for value in [1, 2, 3, 4, 5, 5, 4]:
            s.push(value)
        print(s)

    def test_pop_4(self):
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

    def test_top_4(self):
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

        s.push(30)
        print(s.top())
        s.push(40)
        print(s.top())
        print(s)
        print(s.top())
        s.pop()
        print(s.top())
        print(s)

    # part 5. Queue ADT - Linked Nodes Implementation
    def test_enqueue_5(self):
        print("\n# enqueue example 1")
        q = Queue()
        print(q)
        for value in [1, 2, 3, 4, 5]:
            q.enqueue(value)
        print(q)

    def test_dequeue_5(self):
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

    def test_front_5(self):
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

        print('\n')
        q.enqueue("A")
        print(q)
        q.dequeue()
        print(q)
        print(q.front())


if __name__ == '__main__':
    unittest.main()
