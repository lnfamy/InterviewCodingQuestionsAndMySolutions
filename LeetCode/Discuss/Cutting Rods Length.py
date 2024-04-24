"""
An automated cutting machine is used to cut rods into segments. The cutting machine can only hold a rod of minLength
or more. A rod is marked with the necessary cuts and their lengths are given as an array in the order they are marked.
Determine if it is possible to plan the cuts so the last cut is from a rod at least minLength units long.

Input: rodLengths = {3, 5, 4, 3} and minLength = 9
Output: Possible

Input: rodLengths = {4, 3, 2} and minLength = 7
Output: Possible

Input: rodLengths = {4, 2, 3} and minLength = 7
Output: Impossible

Input: rodLengths = {5, 6, 2} and minLength = 12
Output: Impossible
"""
from typing import List


"""
intuition: it seems to be that we must check whether there are two consecutive elements whose
sum is equal to or bigger than minLength
"""
def sol(rodLengths: List[int], minLength: int) -> bool:
    prev = rodLengths[0]
    for i in range(1, len(rodLengths)):
        if prev + rodLengths[i] >= minLength:
            return True
        prev = rodLengths[i]

    return False
