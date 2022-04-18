def count_sort(arr: StaticArray) -> StaticArray:
    """
    sort the values in non-ascending order using the count sort algorithm

    count number of times each value in array appears
    accumulate count to indicate index position of each value
    distribute each value according to the designated index position


    """
    # find the range of values in 'arr'
    min, max = min_max(arr)
    length = abs(max-min)+1

    # create 'count_arr' to store frequency of each value in the range
    count_arr = StaticArray(length)

    # tally up each value from 'arr'
    for pos in range(arr.length()):
        # identify an index position to add count
        insert_at = max - arr[pos]

        # for the first count, replace 'None' with 0
        if count_arr[insert_at] is None:
            count_arr.set(insert_at, 0)

        # add count in 'count_arr'
        count_arr[insert_at] += 1

    # initialize the accumulator variable
    accum = count_arr[0]

    # iterate through 'count_arr' to shift and accumulate counts
    for pos in range(count_arr.length()-1):
        # replace all 'None's with 0
        if count_arr[pos+1] is None:
            count_arr.set(pos+1, 0)

        # shift each count by one to the right while accumulating counts
        add = count_arr[pos+1]
        count_arr.set(pos+1, accum)
        accum = accum + add

    # reset the starting index to zero
    count_arr[0] = 0

    # create the result array
    sort_arr = StaticArray(arr.length())

    # distribute each value in 'sort_arr' as per noted in 'count_arr'
    for pos in range(arr.length()):
        locator = max - arr[pos]            # index locator for 'count_arr'
        insert_at = count_arr[locator]      # index position for 'sort_arr'

        # place the current value in the designated index
        sort_arr.set(insert_at, arr[pos])
        count_arr[locator] += 1             # increment for repeat(s), if any

    return sort_arr