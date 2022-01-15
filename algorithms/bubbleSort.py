# Algorithm Explination: https://www.geeksforgeeks.org/bubble-sort

def bubbleSort(array):
    comparisons = 0
    swaps = 0

    for i in range(len(array)):
        for j in range(len(array)-i-1):
            comparisons += 1
            if (array[j] > array[j + 1]):
                swaps += 1
                array[j], array[j + 1] = array[j + 1], array[j]
                yield array, j + 1, j, comparisons, swaps
                comparisons = 0
                swaps = 0
            
