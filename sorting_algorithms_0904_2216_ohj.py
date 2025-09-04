# 代码生成时间: 2025-09-04 22:16:42
import numpy as np"""
A module containing various sorting algorithms using Python and NumPy.

This module includes implementations of common sorting algorithms such as
Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, and Quick Sort.
Each algorithm is designed to be clear, concise, and easy to understand, with appropriate
error handling, comments, and documentation.
"""

# Bubble Sort Algorithm
def bubble_sort(arr):
    """Sorts an array using the Bubble Sort algorithm.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.

    Raises:
    ValueError: If the input is not a numpy array.
    """
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")

    n = arr.size
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Selection Sort Algorithm
def selection_sort(arr):
    """Sorts an array using the Selection Sort algorithm.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.

    Raises:
    ValueError: If the input is not a numpy array.
    """
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")

    n = arr.size
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort Algorithm
def insertion_sort(arr):
    """Sorts an array using the Insertion Sort algorithm.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.

    Raises:
    ValueError: If the input is not a numpy array.
    """
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")

    for i in range(1, arr.size):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Merge Sort Algorithm
def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.

    Raises:
    ValueError: If the input is not a numpy array.
    """
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")

    if arr.size == 1:
        return arr
    mid = arr.size // 2
    L = arr[:mid]
    R = arr[mid:]

    return merge(merge_sort(L), merge_sort(R))

def merge(left, right):
    """Merges two sorted arrays into one sorted array.

    Parameters:
    left (numpy.ndarray): The left array.
    right (numpy.ndarray): The right array.

    Returns:
    numpy.ndarray: The merged sorted array.
    """
    result = np.empty(left.size + right.size)
    i = j = k = 0

    while i < left.size and j < right.size:
        if left[i] < right[j]:
            result[k] = left[i]
            i += 1
        else:
            result[k] = right[j]
            j += 1
        k += 1

    while i < left.size:
        result[k] = left[i]
        i += 1
        k += 1

    while j < right.size:
        result[k] = right[j]
        j += 1
        k += 1

    return result

# Quick Sort Algorithm
def quick_sort(arr):
    """Sorts an array using the Quick Sort algorithm.

    Parameters:
    arr (numpy.ndarray): The array to be sorted.

    Returns:
    numpy.ndarray: The sorted array.

    Raises:
    ValueError: If the input is not a numpy array.
    """
    if not isinstance(arr, np.ndarray):
        raise ValueError("Input must be a numpy array.")

    if arr.size <= 1:
        return arr
    pivot = arr[0]
    less = np.array([x for x in arr[1:] if x <= pivot])
    greater = np.array([x for x in arr[1:] if x > pivot])

    return np.concatenate((quick_sort(less), np.array([pivot]), quick_sort(greater)))

# Example usage
if __name__ == "__main__":
    arr = np.array([64, 34, 25, 12, 22, 11, 90])
    print("Original array: ", arr)
    print("Sorted array (Bubble Sort): ", bubble_sort(arr.copy()))
    print("Sorted array (Selection Sort): ", selection_sort(arr.copy()))
    print("Sorted array (Insertion Sort): ", insertion_sort(arr.copy()))
    print("Sorted array (Merge Sort): ", merge_sort(arr.copy()))
    print("Sorted array (Quick Sort): ", quick_sort(arr.copy()))