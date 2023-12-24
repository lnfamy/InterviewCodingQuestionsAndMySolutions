"""
https://leetcode.com/problems/maximum-number-of-balloons/description/
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for i in range(len(text)):
            if text[i] in letters:
                letters[text[i]] += 1

        # for the character b, which appears 1 time in the word balloon, for x instances of b we have
        # the potential for x instances of balloon.
        # this is the same for each of the other letters except for l and o, which appear twice
        b_count = letters.get('b')
        a_count = letters.get('a')
        l_count = letters.get('l') // 2
        o_count = letters.get('o') // 2
        n_count = letters.get('n')

        # by returning the min of these values, we ensure that if either of these don't
        # appear enough times for x numbers of balloon instances, we return the number that CAN happen
        return min(a_count, b_count, l_count, o_count, n_count)


# and a more generalized solution
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def max_patterns(pattern):
            ans = float('inf')
            text_freq = [0] * 26
            pattern_freq = [0] * 26

            for i in range(len(pattern)):
                pattern_freq[ord(pattern[i]) - ord('a')] += 1

            for i in range(len(text)):
                text_freq[ord(text[i]) - ord('a')] += 1

            for i in range(len(text_freq)):
                if pattern_freq[i] > 0:
                    ans = min(ans, text_freq[i] // pattern_freq[i])

            return ans

        ptrn = 'balloon'
        return max_patterns(ptrn)
