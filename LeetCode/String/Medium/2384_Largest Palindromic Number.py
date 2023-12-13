"""
https://leetcode.com/problems/largest-palindromic-number/description/
"""


class Solution:
    def largestPalindromic(self, num: str) -> str:
        # making a sort of dictionary of how many times each digit appears in num
        count = Counter(num)

        # res is made by joining digit occurences of every digit that has an even number of instances
        # in num, in descending order. we'll reverse it later for the end part of the palindrome
        # we also use lstrip to filter out leading zeroes
        res = ''.join(count[i] // 2 * i for i in '9876543210').lstrip('0')

        # choose the middle digit: count[i] % 2 * i results in 0 for numbers that show up an even number of times
        # and equal to i for a number i that shows up an odd number of time
        # this is because even % 2 = 0 and odd % 2 = 1
        mid = max(count[i] % 2 * i for i in count)

        # return the calculated result or a 0 for the edge case of a special input
        return (res + mid + res[:: -1]) or '0'
