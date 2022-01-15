comparisons = 0
swaps = 0

def quickSort(array, left, right):
    global comparisons, swaps

    if left >= right:
        return
    index = left
    random_index = right
    array[right], array[random_index] = array[random_index], array[right]
    swaps += 1
    
    for j in range(left, right):
        yield array, j, index, comparisons, swaps
        comparisons = 0
        swaps = 0
        comparisons += 1
        if array[j] < array[right]:
            swaps += 1
            array[j], array[index] = array[index], array[j]
            index += 1
    array[index], array[right] = array[right], array[index]
    swaps += 1
    yield from quickSort(array, index + 1, right)
    yield from quickSort(array, left, index - 1)
