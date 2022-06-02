# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 6 - Hash Map Implementation - Open Addressing
# Due Date: 6/3/2022
# Description: implement Hash Map that uses open addressing:
#

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
        TODO: Write this implementation
        """
        # remember, if the load factor is greater than or equal to 0.5,
        # resize the table before putting the new key/value pair

        # check the current load factor
        # resize if greater than or equal to 0.5
        if self.table_load() >= 0.5:
            self.resize_table(self._capacity * 2)

        #
        # get the hash
        init = self._hash_function(key)
        hash = init % self._capacity
        prob = 1

        # create a key/value pair class
        pair = HashEntry(key, value)

        # base case
        if self._size == 0:
            self._buckets.set_at_index(hash, pair)
            self._size += 1
            return

        # create a starting bucket and a probe variable
        bucket = self._buckets.get_at_index(hash)

        # check whether the key exists
        exist = self.contains_key(key)

        # traverse the hash map using quadratic probing
        while bucket is not None:
            # if the key exists
            if exist:
                if bucket.key == key:
                    # update the value
                    bucket.value = value
                    return

            # if the key doesn't exist
            else:
                if bucket.is_tombstone is True:
                    # insert the key/value pair
                    bucket.set_at_index(hash, pair)
                    self._size += 1
                    return

            # update quadratic probing
            hash = (init + (prob ** 2)) % self._capacity
            bucket = self._buckets.get_at_index(hash)
            # increment the probe variable
            prob += 1

        # insert the key/value pair
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
        TODO: Write this implementation
        base case:
        - new_capacity is less than 1
        - new_capacity is less than the number of elements in the map
        """
        # remember to rehash non-deleted entries into new table

        # base case
        if new_capacity < 1 or new_capacity < self._size:
            return

        # store the current capacity
        old_capacity = self._capacity
        self._capacity = new_capacity

        # double the capacity if load factor is greater than or equal to 0.5
        while self.table_load() >= 0.5:
            self._capacity = self._capacity * 2

        # create a new map
        new_map = DynamicArray()
        for _ in range(self._capacity):
            new_map.append(None)

        #
        for pos in range(old_capacity):
            curr = self._buckets.get_at_index(pos)
            if curr is not None and curr.is_tombstone is False:
                # rehash
                init = self._hash_function(curr.key)
                hash = init % self._capacity
                dest = new_map.get_at_index(hash)
                prob = 1
                #
                while dest is not None:
                    hash = (init + (prob ** 2)) % self._capacity
                    dest = new_map.get_at_index(hash)
                    prob += 1
                #
                pair = HashEntry(curr.key, curr.value)
                new_map.set_at_index(hash, pair)

        # update the hash table and its capacity
        self._buckets = new_map

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
            # keep probing until the key is found
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
        if self.get(key) is not None:
            return True

        return False

    def remove(self, key: str) -> None:
        """
        TODO: Write this implementation
        base case:
        (1) empty hash map; nothing to remove
        (2) key doesn't exist; nothing to remove
        """
        # base case (1) & (2)
        if self._size == 0 or self.contains_key(key) is False:
            return

        # initialize the starting place to search the key
        init = self._hash_function(key)
        hash = init % self._capacity
        bucket = self._buckets.get_at_index(hash)

        # create a probe variable
        probe = 1

        # loop through the hash map to find the key
        while bucket:
            # keep probing until the key is found
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

    def clear(self) -> None:
        """
        clears the hash map table without changing its capacity
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
