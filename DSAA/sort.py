import numpy as np


def selectionSort(arr: list):
    n = len(arr)

    for i in range(n):
        index = i
        for j in range(i+1, n):
            if arr[j] < arr[index]:
                index = j
        template = arr[index]
        arr[index] = arr[i]
        arr[i] = template
    return arr


a = [3, 5, 1, 2, 10, 5]
b = selectionSort(a)
print(b)
