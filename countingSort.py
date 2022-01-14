# Algorithm Explination: https://www.geeksforgeeks.org/counting-sort

def countingSort(size, array):

    # Create the dictionary
    count = {}
    for i in range(size):
        count[i] = 0

    # STEP 1:
    for i in range(len(array)):
        count[array[i]] += 1

    # STEP 2:
    for i in range(1, size):
        count[i] = count[i] + count[i-1]

    # STEP 3:
    output = array.copy()
    for i in range(len(array)):
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        yield output, count[array[i]] - 1, -2
