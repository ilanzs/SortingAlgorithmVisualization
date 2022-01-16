def gnomeSort(array):
    comparisons, swaps = 0, 0
    index = 0
    while index < len(array) - 1:
        if index == 0: index += 1
        comparisons += 2
        if array[index] >= array[index - 1]: index += 1
        if array[index] < array[index - 1]:
            swaps += 1
            array[index], array[index - 1] = array[index - 1], array[index]
            index -= 1
        yield array, index, index - 1, comparisons, swaps
        comparisons, swaps = 0, 0
