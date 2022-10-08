# Name: GinWook Lee
# OSU Email: leeginw@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2 - Dynamic Array Implementation Part 1
# Due Date: 4/25/2022
# Description: implement Dynamic Array class that can perform the following:
#   1) resize(): adjust the capacity based on the number of elements
#   2) append(): add a new value at the end of the array
#   3) insert_at_index(): add a new value at the specified index in the array
#   4) remove_at_index(): remove a value at the specified index in the array
#   5) slice(): fetch value(s) within a specified portion of the array
#   6) merge(): append an entire array to another one
#   7) map(): apply a function to each element in the array
#   8) filter(): select only the value(s) that passes certain criteria
#   9) reduce(): derive one value from sequential application(s) of a function
#
#   Standalone function outside the Dynamic Array class:
#   find_mode(): detect the most occurring value(s) and the highest frequency

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
        """
        expand the capacity without changing the content in the dynamic array

        base cases:
        (1) new_capacity is not a positive integer
        (2) new_capacity is less than the current size
        """
        # base cases
        if new_capacity <= 0:
            return                              # (1)
        if new_capacity < self._size:
            return                              # (2)

        # create a new StaticArray
        new_sa = StaticArray(new_capacity)

        # copy values from the old to new StaticArray
        for pos in range(self._size):
            new_sa[pos] = self._data.get(pos)

        # the new becomes the current array
        self._data = new_sa
        self._capacity = new_capacity

    def append(self, value: object) -> None:
        """
        add a new value at the end of the dynamic array

        if the array is full, double the capacity before appending
        """
        # double the capacity if the capacity is full
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
            self.resize(new_capacity)

        # append a new value and increment the size
        self._data.set(self._size, value)
        self._size += 1

    def insert_at_index(self, index: int, value: object) -> None:
        """
        insert 'value' at 'index' in the dynamic array
        subsequent elements move one index up (or, to the right)

        exception case: invalid index
        (1) valid indices for 'size' N are [0, N] inclusive
        """
        # exception case
        if index < 0 or index > self._size:
            raise DynamicArrayException         # (1)

        # when the array is already full, double the capacity
        if self._size == self._capacity:
            new_capacity = self._capacity * 2
            self.resize(new_capacity)

        # insert and push each subsequent value up by one
        for plus in range(self._size + 1 - index):
            temp = self._data.get(index + plus)
            self._data.set(index + plus, value)
            value = temp

        # adjust the array size
        self._size += 1

    def remove_at_index(self, index: int) -> None:
        """
        remove a value at the specified 'index' in the dynamic array
        values following the removed content, if any, shift down by one index

        exception case:
        - other than valid indices for the array size N, [0, N-1] inclusive
        base case:
        - empty array (nothing to remove)
        """
        # exception case
        if index < 0 or index > (self._size - 1):
            raise DynamicArrayException

        # base case
        if self._size == 0:
            return

        # capacity adjustment before removal
        if (self._size * 4) < self._capacity and self._capacity > 10:
            if (self._size * 2) > 10:
                self.resize(self._size * 2)
            else:
                self.resize(10)                 # min capacity when reduced

        # remove at index and shift down each subsequent value by one
        for plus in range(self._size - index - 1):
            self._data.set(index + plus, self._data.get(index + plus + 1))

        # adjust the array size
        self._size -= 1

    def slice(self, start_index: int, size: int) -> "DynamicArray":
        """
        fetch value(s) within a specified portion of the array:
        - 'size' specifies the number of elements
        - 'start_index' specifies where to begin slicing the array

        return 'slice_arr'

        exception cases:
        (1) other than valid indices for the array size N, [0, N-1] inclusive
        (2) negative 'size' or 'size' bigger than the array size
        (3) requesting elements beyond the end of the array
        """
        # exception cases
        if start_index < 0 or start_index > (self._size - 1):
            raise DynamicArrayException         # (1)
        if size < 0 or size > self._size:
            raise DynamicArrayException         # (2)
        if start_index + size > self._size:
            raise DynamicArrayException         # (3)

        # create a new array
        slice_arr = DynamicArray()

        # slice from the dynamic array and append to 'sliced_arr'
        for plus in range(size):
            val = self.get_at_index(start_index + plus)
            slice_arr.append(val)

        return slice_arr

    def merge(self, second_da: "DynamicArray") -> None:
        """
        append all values in 'second_da' to the current dynamic array
        """
        # append each value in 'second_da' to the dynamic array one at a time
        for pos in range(second_da.length()):
            self.append(second_da.get_at_index(pos))

    def map(self, map_func) -> "DynamicArray":
        """
        1) apply 'map_func' to each value in the dynamic array
        2) append those applied values to the new array, 'map_arr'

        return 'map_arr'
        """
        # create a new array
        map_arr = DynamicArray()

        # append to 'map_arr' after applying 'map_func' to each element
        for pos in range(self._size):
            val = self.get_at_index(pos)
            map_arr.append(map_func(val))

        return map_arr

    def filter(self, filter_func) -> "DynamicArray":
        """
        load only the values that pass criteria in 'filter_func'

        return 'filt_arr'
        """
        # create a new array
        filt_arr = DynamicArray()

        # append only the values that pass 'filter_func' to 'filt_arr'
        for pos in range(self._size):
            val = self.get_at_index(pos)

            # append only when 'filter_func' returns True
            if filter_func(val) is True:
                filt_arr.append(val)

        return filt_arr

    def reduce(self, reduce_func, initializer=None) -> object:
        """
        apply 'reduce_func' to each value sequentially and return the result

        return the resulting value (stored in 'initializer')

        base case:
        - empty dynamic array returns initializer or None
        """
        # base case
        if self._size == 0:
            return initializer

        # index adjustment depending on the initial 'initializer' setting
        adj = 0

        # set 'initializer' if not provided
        if initializer is None:
            initializer = self.get_at_index(0)
            adj = 1

        # apply 'reduce_func' and update result on 'initializer' sequentially
        for pos in range(self._size - adj):
            val = self.get_at_index(pos + adj)
            initializer = reduce_func(initializer, val)

        return initializer


def find_mode(arr: DynamicArray) -> (DynamicArray, int):
    """
    identify the mode value(s) in 'arr'

    return mode(s) and the highest frequency
    """
    # set initial variables for finding the highest frequency
    count = 1
    freq = 1

    # fetch the highest frequency
    for pos in range(arr.length() - 1):
        # compare two consecutive values
        if arr.get_at_index(pos) == arr.get_at_index(pos + 1):
            count += 1
            if count > freq:
                freq = count                    # update 'freq'
        else:
            count = 1                           # reset 'count'

    # create a new array
    mode = DynamicArray()

    # when 'freq' equals 1, each value is a mode
    if freq == 1:
        mode.merge(arr)
        return mode, freq

    # reset 'count' for finding the mode(s)
    count = 1

    # append to 'mode' only when 'count' matches 'freq'
    for pos in range(arr.length() - 1):
        # compare two consecutive values
        if arr.get_at_index(pos) == arr.get_at_index(pos + 1):
            count += 1
        else:
            count = 1                           # reset 'count'

        if count == freq:
            mode.append(arr.get_at_index(pos))  # append a mode

    return mode, freq

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

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

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")

    # update git comment