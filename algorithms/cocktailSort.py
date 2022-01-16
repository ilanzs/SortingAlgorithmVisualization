def cocktailSort(array):
    comparisons = 0
    swaps = 0
    n = len(array)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
        swapped = False
        for i in range (start, end):
            comparisons += 1
            if (array[i] > array[i+1]):
                swaps += 1
                array[i], array[i+1]= array[i+1], array[i]
                swapped=True
            yield array, i, i + 1, comparisons, swaps
            comparisons, swaps = 0, 0
            
        
        if (swapped==False):
            break

        swapped = False

        end = end-1

        for i in range(end-1, start-1,-1):
            comparisons += 1
            if (array[i] > array[i+1]):
                swaps += 1
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
            yield array, i, i + 1, comparisons, swaps
            comparisons, swaps = 0, 0
        start = start + 1

