def shellSort(array):
    comparisons = 0
    swaps = 0

    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    
    for gap in gaps:
        for offset in range(gap):
            i = offset
            while i < len(array):
                comparisons += 1
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    swaps += 1
                    array[j] = array[j - gap]
                    j -= gap
                swaps += 1
                array[j] = temp
                i += gap
                yield array, j, j - gap, comparisons, swaps
                comparisons = 0
                swaps = 0






