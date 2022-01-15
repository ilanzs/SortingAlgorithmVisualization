from math import floor

comparisons = 0
swaps = 0

def stoogeSort(array, i = 0, j = None):
    global comparisons, swaps

    if j == None:
        j = len(array) - 1
    comparisons += 1
    if array[i] > array[j]:
        swaps += 1
        array[i], array[j] = array[j], array[i]
    if (j - i + 1) > 2:
        t = floor((j - i + 1) / 3)
        yield from stoogeSort(array, i, j - t)
        yield from stoogeSort(array, i + t, j)
        yield from stoogeSort(array, i, j - t)

        yield array, i, j, comparisons, swaps
        comparisons = 0
        swaps = 0



