"""
https://leetcode.com/problems/stream-of-characters/description/
"""
from collections import deque
from typing import List


class StreamChecker:
    """
    approach: construct a reverse trie of all the words in words[]
    since we always know what the last character of what we want to match is
    in this way we can immediately compare the last character received with the last character
    of the matching-candidate suffixes
    """

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = deque([])

        for word in set(words):
            node = self.trie
            # for character in the reversed word
            for ch in word[::-1]:
                if not ch in node:
                    node[ch] = {}
                # advance to next node in trie
                node = node[ch]
            # $ marks the end of a 'word' or in our case, suffix
            node['$'] = word

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)

        node = self.trie
        for ch in self.stream:
            # we return true only if the entire suffix is here - that is to say,
            # we've reached the end of the suffix comparison with no problems
            if '$' in node:
                return True
            # if at any point we find a mismatch, return False immediately
            if not ch in node:
                return False
            # advance to next character
            node = node[ch]
        # returns true if encountered '$' (entire suffix is here), false otherwise
        return '$' in node



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)