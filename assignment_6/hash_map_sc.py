# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 - Hash Map Implementation - Chaining
# Due Date: 6/3/2022
# Description: implement Hash Map that uses chaining:
#   1) put(): add or replace a key / value pair
#   2) get(): fetch a value associated with the given key
#   3) remove(): remove a key / value pair based on the given key
#   4) contains_key(): check whether the given key already exists
#   5) clear(): remove all the contents while maintaining the capacity
#   6) empty_buckets(): count the number of empty buckets
#   7) resize_table(): update the capacity and rehash all contents accordingly
#   8) table_load(): calculate the current load factor
#   9) get_keys(): list all the keys in a form of a dynamic array
#
#   standalone function outside the HashMap class
#   find_mode(): find the most occurring value(s) and its frequency

from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(LinkedList())

        self._capacity = capacity
        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #

    def put(self, key: str, value: object) -> None:
        """
        update the hash map using 'key' and 'value'

        if 'key' already exists, update it with new 'value'
        if not, add a new 'key'/'value' pair

        base case:
        - empty hash map; insert
        """
        # get the hash index
        hash = self._hash_function(key) % self._capacity

        # find the right bucket
        buck = self._buckets.get_at_index(hash)

        # base case
        if self._size == 0:
            # insert and update the size
            buck.insert(key, value)
            self._size += 1
            return

        # check if the key already exists
        node = buck.contains(key)
        # if yes, update the node
        if node:
            node.value = value
        # if no, insert and update the size
        else:
            buck.insert(key, value)
            self._size += 1

    def empty_buckets(self) -> int:
        """
        count the number of empty buckets

        return the count
        """
        # initiate a count variable
        count = 0

        # iterate through each bucket to check whether it's empty
        for buck in range(self._capacity):
            if self._buckets.get_at_index(buck).length() == 0:
                count += 1

        return count

    def table_load(self) -> float:
        """
        return the hash load factor

        self._size == # of key/value pairs
        self._capacity == # of buckets
        """
        return self._size / self._capacity

    def clear(self) -> None:
        """
        clears the hash map table without changing its capacity
        """
        # reset Dynamic Array
        self._buckets = DynamicArray()
        # append an empty LinkedList class for each bucket
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        # reset the size
        self._size = 0

    def resize_table(self, new_capacity: int) -> None:
        """
        change the capacity while rehashing all the existing key/value pairs

        base case:
        - new_capacity is less than 1
        - new_capacity equals to the current capacity
        """
        # base case
        if new_capacity < 1 or new_capacity == self._capacity:
            return

        # copy the current bucket
        cur_buck = self._buckets
        # create a new empty bucket
        new_buck = DynamicArray()
        # switch to the new bucket
        self._buckets = new_buck
        for _ in range(new_capacity):
            self._buckets.append(LinkedList())

        # store the current capacity and update to the new capacity
        cur_capacity = self._capacity
        self._capacity = new_capacity

        # reset the size
        self._size = 0

        # iterate through the current bucket
        for _ in range(cur_capacity):
            link = cur_buck.pop()
            for node in link:
                self.put(node.key, node.value)

    def get(self, key: str) -> object:
        """
        return the value associated with 'key' if 'key' exists
        Otherwise, return None
        """
        # find the right bucket
        hash = self._hash_function(key) % self._capacity
        buck = self._buckets.get_at_index(hash)

        # return the value if 'key' exists
        res = buck.contains(key)
        if res:
            return res.value

        return None

    def contains_key(self, key: str) -> bool:
        """
        return True if 'key' exists
        Otherwise, return False

        base case:
        - empty hash map; contains nothing
        """
        # base case
        if self._size == 0:
            return False

        # find the right bucket
        hash = self._hash_function(key) % self._capacity
        buck = self._buckets.get_at_index(hash)

        # check if the key exists
        if buck.contains(key):
            return True

        return False

    def remove(self, key: str) -> None:
        """
        remove the first node associated with 'key'
        """
        # find the right bucket
        hash = self._hash_function(key) % self._capacity
        buck = self._buckets.get_at_index(hash)

        # remove the value if 'key' exists
        res = buck.remove(key)

        if res is True:
            # update size
            self._size -= 1

    def get_keys(self) -> DynamicArray:
        """
        get all the keys stored in the hash map

        return the result as a Dynamic Array

        base case:
        - empty hash map; return an empty dynamic array
        """
        # create a new DA
        new_da = DynamicArray()

        # base case
        if self._size == 0:
            return new_da

        # loop through each bucket at a time
        for buck in range(self._capacity):
            # start with the linked list at the end
            link = self._buckets.get_at_index(buck)
            # iterate through the current linked list, if any
            for node in link:
                # append each key to the new DA
                new_da.append(node.key)

        return new_da


def find_mode(da: DynamicArray) -> (DynamicArray, int):
    """
    find the mode and the highest frequency in the given 'da'

    use hash map features to return a tuple that contains:
    - the mode as a dynamic array
    - the highest frequency as an integer
    """
    # create a hash map
    map = HashMap(da.length() // 3, hash_function_1)

    # initialize mode and frequency variables
    mod = DynamicArray()                        # empty dynamic array
    frq = 1                                     # assume at least one element

    # loop through each element in the given dynamic array
    for pos in range(da.length()):
        # store key and value variables
        key = da.get_at_index(pos)
        val = map.get(key)

        # value is 1 if the key doesn't exist. Otherwise, increment the value
        val = 1 if val is None else val + 1

        # update the hash map using the key and the value
        map.put(key, val)

        # if the value equals the frequency
        if val == frq:
            mod.append(key)                     # append the key
        # if the value is greater than the frequency
        elif val > frq:
            mod = DynamicArray()                # reset the array
            mod.append(key)                     # append the key
            frq = val                           # update the frequency

    return mod, frq


# ------------------- BASIC TESTING ---------------------------------------- #

if __name__ == "__main__":

    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())

    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.get_size(), m.get_capacity())

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())

    print("\nPDF - find_mode example 1")
    print("-----------------------------")
    da = DynamicArray(["apple", "apple", "grape", "melon", "melon", "peach"])
    map = HashMap(da.length() // 3, hash_function_1)
    mode, frequency = find_mode(da)
    print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}")

    print("\nPDF - find_mode example 2")
    print("-----------------------------")
    test_cases = (
        ["Arch", "Manjaro", "Manjaro", "Mint", "Mint", "Mint", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"],
        ["one", "two", "three", "four", "five"],
        ["2", "4", "2", "6", "8", "4", "1", "3", "4", "5", "7", "3", "3", "2"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        map = HashMap(da.length() // 3, hash_function_2)
        mode, frequency = find_mode(da)
        print(f"Input: {da}\nMode: {mode}, Frequency: {frequency}\n")
