def count_sort(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    #
    min, max = min_max(arr)

    # use sa_range(max, min) to create a dummy StaticArray
    dum_arr = sa_range(max, min)
    count_arr = StaticArray(dum_arr.length())

    count = 0

    # count each value
    for pos in range(dum_arr.length()):
        for idx in range(arr.length()):
            if dum_arr[pos] == arr[idx]:
                count += 1
                count_arr[pos] = count

        count = 0

    #

    return count_arr