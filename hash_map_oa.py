# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 - Hash Map Implementation - Open Addressing
# Due Date: 6/3/2022
# Description: implement Hash Map that uses open addressing:
#   1) put(): add or replace a key/value pair
#   2) get(): fetch a value associated with the given key
#   3) remove(): remove a key/value pair based on the given key
#   4) contains_key(): check whether the given key already exists
#   5) clear(): remove all the contents while maintaining the capacity
#   6) empty_buckets(): count the number of empty buckets
#   7) resize_table(): update the capacity and rehash all contents accordingly
#   8) table_load(): calculate the current load factor
#   9) get_keys(): list all the keys in a form of a dynamic array

from a6_include import (DynamicArray, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()
        for _ in range(capacity):
            self._buckets.append(None)

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
        # check the current load factor
        if self.table_load() >= 0.5:
            # resize if greater than or equal to 0.5
            self.resize_table(self._capacity * 2)

        # get the first hash variable and initialize a probe value
        init = self._hash_function(key)
        hash = init % self._capacity
        prob = 1

        # create the key/value pair as a HashEntry class
        pair = HashEntry(key, value)

        # base case
        if self._size == 0:
            self._buckets.set_at_index(hash, pair)
            self._size += 1
            return

        # identify the starting bucket
        bucket = self._buckets.get_at_index(hash)

        # traverse the hash map using quadratic probing
        while bucket is not None and bucket.is_tombstone is False:
            # update the existing key
            if bucket.key == key:
                # update the value
                bucket.value = value
                return

            # update quadratic probing
            hash = (init + (prob ** 2)) % self._capacity
            bucket = self._buckets.get_at_index(hash)
            # increment the probe variable
            prob += 1

        # insert the key/value pair when the bucket is None or is a tombstone
        self._buckets.set_at_index(hash, pair)
        self._size += 1

    def table_load(self) -> float:
        """
        return the hash load factor

        self._size == # of key/value pairs
        self._capacity == # of buckets
        """
        return self._size / self._capacity

    def empty_buckets(self) -> int:
        """
        count the number of empty buckets

        return the count
        """
        return self._capacity - self._size

    def resize_table(self, new_capacity: int) -> None:
        """
        change the capacity while rehashing all the existing key/value pairs

        base case:
        - new_capacity is less than 1
        - new_capacity is less than the number of elements in the map
        """
        # base case
        if new_capacity < 1 or new_capacity < self._size:
            return

        # create a new hash map
        new_map = HashMap(new_capacity, self._hash_function)

        # loop through the old bucket
        for _ in range(self._capacity):
            curr = self._buckets.get_at_index(_)
            # copy to the new hash map if 'curr' contains a live pair
            if curr is not None and curr.is_tombstone is False:
                new_map.put(curr.key, curr.value)

        # update the hash map properties
        self._buckets = new_map._buckets
        self._capacity = new_map._capacity

    def get(self, key: str) -> object:
        """
        return the value associated with 'key' if 'key' exists
        Otherwise, return None

        base case:
        - empty hash map; nothing to get
        """
        # base case
        if self._size == 0:
            return None

        # initialize the starting place to search the key
        init = self._hash_function(key)
        hash = init % self._capacity
        bucket = self._buckets.get_at_index(hash)

        # create a probe variable
        probe = 1

        # loop through the hash map to find the key
        while bucket is not None:
            # keep probing if 'bucket' is a tombstone or its key doesn't match
            if bucket.is_tombstone is True or bucket.key != key:
                # quadratic probing
                hash = (init + (probe ** 2)) % self._capacity
                bucket = self._buckets.get_at_index(hash)
                # increment the probe variable
                probe += 1

            # found the key
            else:
                return bucket.value

        # key not found
        return None

    def contains_key(self, key: str) -> bool:
        """
        return True if 'key' exists
        Otherwise, return False
        """
        if self.get(key) is None:
            return False

        return True

    def remove(self, key: str) -> None:
        """
        remove a HashEntry class associated with 'key'

        base case:
        - empty hash map; nothing to remove
        """
        # base case
        if self._size == 0:
            return

        # initialize the starting place to search the key
        init = self._hash_function(key)
        hash = init % self._capacity
        bucket = self._buckets.get_at_index(hash)

        # create a probe variable
        probe = 1

        # loop through the hash map to find the key
        while bucket is not None:
            # keep probing if 'bucket' is a tombstone or its key doesn't match
            if bucket.is_tombstone is True or bucket.key != key:
                # quadratic probing
                hash = (init + (probe ** 2)) % self._capacity
                bucket = self._buckets.get_at_index(hash)
                # increment the probe variable
                probe += 1

            # found the key
            else:
                # remove the key/value pair by setting a tombstone
                bucket.is_tombstone = True
                # decrement the size
                self._size -= 1

                return

        # key not found
        return

    def clear(self) -> None:
        """
        clear the hash map table without changing its capacity
        """
        # reset the dynamic array
        self._buckets = DynamicArray()
        # append None for each bucket
        for _ in range(self._capacity):
            self._buckets.append(None)

        # reset the size
        self._size = 0

    def get_keys(self) -> DynamicArray:
        """
        get all the keys stored in the hash map

        return the result as a Dynamic Array

        base case:
        - empty hash map; return an empty dynamic array
        """
        # create a new Dynamic Array
        new_da = DynamicArray()

        # base case
        if self._size == 0:
            return new_da

        # loop through each bucket at a time
        for buck in range(self._capacity):
            curr = self._buckets.get_at_index(buck)
            # append a key to the new DA if curr is not empty
            if curr is not None and curr.is_tombstone is False:
                new_da.append(curr.key)

        return new_da


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

        if m.table_load() >= 0.5:
            print("Check that capacity gets updated during resize(); "
                  "don't wait until the next put()")

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
