"""
https://leetcode.com/problems/minimum-suffix-flips/
"""


class Solution:
    # naive approach. gives TLE on bigger inputs
    def minFlips(self, target: str) -> int:
        lst = '0' * len(target)
        s = ''.join(lst)
        num_flips = 0

        def flip(index):
            copy = list(s)
            for i in range(index, len(copy)):
                if copy[i] == '0':
                    copy[i] = '1'
                else:
                    copy[i] = '0'
            return ''.join(copy)

        for i in range(len(target)):
            if s == target:
                return num_flips
            if s[i] != target[i]:
                s = flip(i)
                num_flips += 1

        return num_flips

    # smarter approach
    def minFlips_v2(self, target: str) -> int:
        # initial string is 00000...
        # in this approach we'll "pretend" that we're making the flips happen.
        # this saves up a lot of resources while also giving us the answer we need.
        num_flips = 0
        all_ones = False
        for i in range(len(target)):
            if all_ones:
                if target[i] == '0':
                    num_flips += 1
                    all_ones = False
            else:
                if target[i] == '1':
                    num_flips += 1
                    all_ones = True
        return num_flips
