from typing import List

"""
You are given an array given of size . The next element is +K or -K of the previous element: 
ex. a[i+1]=a[i]+k or a[i+1]=a[i]-k
given an element X, return it's index if it's present in array or -1.
"""


def naive_sol(arr: List[int], x: int, k: int):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

    return -1


def binary_search_sol(arr: List[int], x: int, k: int):
    low = 0
    high = len(arr) - 1
    while low <= high:
        # base case
        if low == high:
            return low if arr[low] == x else -1

        mid = (low + high) // 2
        # if arr[mid] is greater than +k, +k, ... +k, there's no way the answer will be to the left of mid
        if arr[mid] > (arr[low] + ((mid - low)* k)):
            low = mid
        elif arr[mid] < (arr[high] + ((high - mid) * k)):
            high = mid
        else:
            for i in range(low, high):
                if arr[i] == x:
                    return i

    return -1