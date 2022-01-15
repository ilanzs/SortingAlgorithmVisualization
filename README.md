# SortingAlgorithmVisualization

A place for me to learn about sorting algorithms.

## Getting started

1. Install python on your machine.
2. Install pygame by running this command: ```pip install pygame```.
3. Navigate to the folder at which ```main.py``` is located.
4. In your terminal run ```python main.py <sortingAlgorithm>```

## How to navigate the GUI

To increase the number of elements in the array press the <kbd>↑</kbd>.\
To decrease the number of elements in the array press the <kbd>↓</kbd>.\
To increase the sorting speed press the <kbd>→</kbd>.\
to decrease the sorting speed press the <kbd>←</kbd>.

## Implemented sorting algorithms

### [Counting Sort](https://www.geeksforgeeks.org/counting-sort)

Counting Sort is a good algorithm for lists with small positive integer\
Speed: O(n+k)\
n is number of elements in the array.
k is range of possible numbers in the array.

### [Bubble Sort](https://www.geeksforgeeks.org/bubble-sort)

Bubble Sort a simple inefficient sorting algorithms. Works with any float or integer\
Speed: Speed: O(n²)\
n is number of elements in the array.

### [Quick Sort](https://www.geeksforgeeks.org/quick-sort/)

Quick Sort is a divide and conquer sorting algorithm.\
Speed: O(n log n)\
n is number of elements in the array.

### [Merge Sort](https://www.geeksforgeeks.org/merge-sort/)

Merge Sort is a divide and conquer sorting algorithm.\
Speed: O(n log n)\
n is number of elements in the array.

### [Comb Sort](https://en.wikipedia.org/wiki/Comb_sort)

Comb Sort is an imporvement on Bubble Sort.\
Speed: O(n² / 2<sup>p</sup>)
n is number of elements in the array.
p is number of increments.

### [Shell Sort](https://en.wikipedia.org/wiki/Comb_sort)

Shell Sort is an in place compirason sort.
Speed: Worst:  O(n²)
       Best:   O(n log n)
n is number of elements in the aray.

### [Bogo Sort](https://www.geeksforgeeks.org/bogosort-permutation-sort)

Bogo Sort is made as a joke. It works by shuffling the list until it is sorted.\
Speed: O((n + 1)!)\
n is number of elements in the array.
