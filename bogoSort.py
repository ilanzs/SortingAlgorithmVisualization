import random

# # Algorithm Explination: https://www.geeksforgeeks.org/bogosort-permutation-sort

def bogoSort(array):
    while True:
        random.shuffle(array)
        yield array, -2

