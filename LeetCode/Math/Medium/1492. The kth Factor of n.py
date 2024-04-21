"""
https://leetcode.com/problems/the-kth-factor-of-n/description/
"""


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, int(n ** 0.5) + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        """
        if we got here, we have two options:
            1. k is too big, ie. there's not a kth factor for n
            2. n is the result of squaring an integer.
        if sqrt(n) is an inteer, we can't double count sqrt(n). 
        """
        # descending run back to 0 from the square root
        # this loop takes care of the case where n is a perfect square
        for i in range(int(n ** 0.5), 0, -1):
            # skipping the double count
            if i ** 2 == n: continue
            if n % i == 0:
                k -= 1
                if k == 0:
                    return n // i

        return -1
