def selectionSort(array):
    comparisons = 0
    swaps = 0
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            comparisons += 1
            if array[minimum_index] > array[j]:
                minimum_index = j
                yield array, i, minimum_index, comparisons, swaps
                comparisons = 0
                swaps = 0
        
        swaps += 1
        array[i], array[minimum_index], = array[minimum_index], array[i]

        


