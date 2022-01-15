from math import floor

def combSort(array):
    comparisons = 0
    swaps = 0
    gap = len(array)
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        gap = floor(gap / shrink)
        if gap <= 1:
            is_sorted = True
            gap = 1

        for i in range(len(array) - gap):
            comparisons += 1
            sum = gap + i
            if array[i] > array[sum]:
                swaps += 1
                array[i], array[sum] = array[sum], array[i]
                is_sorted = False

            yield array, i, sum, comparisons, swaps
            comparisons = 0
            swaps = 0


