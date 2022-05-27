import unittest
from hash_map_sc import *


class TestHashMap(unittest.TestCase):
    """ """
    def test_put(self):
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

    def test_empty_buckets(self):
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

    def test_table_load(self):
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

    def test_clear(self):
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


if __name__ == '__main__':
    unittest.main()
