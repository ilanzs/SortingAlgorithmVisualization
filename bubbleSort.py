# Algorithm Explination: https://www.geeksforgeeks.org/bubble-sort

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]
                yield array, j
