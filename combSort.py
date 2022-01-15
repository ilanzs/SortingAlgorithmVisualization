from math import floor

def combSort(array):
    gap = len(array)
    shrink = 1.3
    is_sorted = False

    while not is_sorted:
        gap = floor(gap / shrink)
        if gap <= 1:
            is_sorted = True
            gap = 1

        for i in range(len(array) - gap):
            sum = gap + i
            if array[i] > array[sum]:
                array[i], array[sum] = array[sum], array[i]
                is_sorted = False

            yield array, i, sum
