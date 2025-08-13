# 代码生成时间: 2025-08-14 04:10:20
import numpy as np

"""
Sorting Algorithm Implementation

This module provides various sorting algorithms implemented in Python using NumPy for efficient array operations.
It includes Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort, and Heap Sort.

Attributes:
    None

Methods:
    bubble_sort(arr): Sorts an array using Bubble Sort algorithm.
    selection_sort(arr): Sorts an array using Selection Sort algorithm.
    insertion_sort(arr): Sorts an array using Insertion Sort algorithm.
    merge_sort(arr): Sorts an array using Merge Sort algorithm.
    quick_sort(arr): Sorts an array using Quick Sort algorithm.
    heap_sort(arr): Sorts an array using Heap Sort algorithm.
"""

def bubble_sort(arr):
    """Sorts an array using Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    """Sorts an array using Selection Sort algorithm."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Sorts an array using Insertion Sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def merge_sort(arr):
    """Sorts an array using Merge Sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    """Sorts an array using Quick Sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

def heapify(arr, n, i):
    """Helper function to heapify an array."""
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Sorts an array using Heap Sort algorithm."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Example usage
if __name__ == "__main__":
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
    print("Original array: ", arr)
    sorted_arr = quick_sort(arr.copy().tolist())  # Using Quick Sort for demonstration
    print("Sorted array: ", sorted_arr)