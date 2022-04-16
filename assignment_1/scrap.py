# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    # base case: only one value in 'arr'
    if arr.length() == 1:
        return 1

    #
    lead = 0

    if arr[0] < arr[1]:                     # ascending
        sign = 1

    if arr[0] > arr[1]:                     # descending
        sign = -1

    #
    for pos in range(arr.length()-1):
        if arr[pos] < arr[pos+1]:           # ascending
            lead += 1

            if sign != 1:
                return 0

        elif arr[pos] > arr[pos+1]:         # descending
            lead -= 1

            if sign != -1:
                return 0

        else:
            return 0                        # two same values

    return lead // (arr.length()-1)
