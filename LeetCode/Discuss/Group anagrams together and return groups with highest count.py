"""
Given an array of strings strs, group the anagrams together and return all the groups which have the highest count
An anagram is a word of phrase formed by rearranging the letters of a different word or phrase, typically using all
the original letters exactly once.

Input:
First line contains number of strings
Second line contains array of string literals in lowercase

output:
returns the group of string literals which has max count (in separate lines if the max count is same in any order)
"""


"""
THIS IS A MODIFICATION OF THE LEETCODE QUESTION: 49. Group Anagrams
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We start by initializing an empty unordered map called anagram_map, which will store the groups of anagrams.
        anagram_map = defaultdict(list)
        # We iterate through each word in the input vector strs.
        # We create a string variable called sorted_word and assign it the value of the current word.
        # Next, we sort the characters in word using the sorted() function.
        # We insert word as the key into the anagram_map unordered map using anagram_map[sorted_word],
        # and we push the original word into the vector associated with that key using anagram_map[sorted_word].append(word),
        # where word is the current word.
        # Since sorted_word is a unique sorted representation of all the anagrams, it serves as the key in the anagram_map map,
        # and the associated vector holds all the anagrams.
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        # For the given example, the anagram_map map would look like this after processing all the words:
        # {
        #   "aet": ["eat", "tea", "ate"],
        #   "ant": ["tan", "nat"],
        #   "abt": ["bat"]
        # }
        # We return the list, which contains the groups of anagrams.

        # find the longest list length of anagrams
        anagram_list = list(anagram_map.values())
        length = 0
        for ls in anagram_list:
            length = max(length, len(ls))

        res = []
        # append to result only the anagram lists that are at the max length
        for ls in anagram_list:
            if len(ls) == length:
                res.append(ls)

        return res