def mergeSort(array, left, right):
    if left < right:
        middle = int((left + right) / 2)
        yield from mergeSort(array, left, middle)
        yield from mergeSort(array, middle + 1, right)
        yield from merge(array, left, middle, right)


def merge(array, left, middle, right):
    left_array = array[left:middle + 1]
    right_array = array[middle + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        yield array, k, middle + j
        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1

        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1
    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1
      
    