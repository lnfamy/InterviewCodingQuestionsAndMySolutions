"""
https://leetcode.com/problems/text-justification/description/
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # function to decide how many words can go in one line
        def words_line(i: int):
            words_in_line = []
            num_words = 0
            num_characters = 0
            while i < len(words) and num_characters + len(words[i]) <= maxWidth:
                num_characters += len(words[i]) + 1
                words_in_line.append(words[i])
                i += 1
            return words_in_line

        def make_line(words_in_line, num_line):
            num_chars = -1
            for word in words_in_line:
                num_chars += len(word) + 1

            spaces = maxWidth - num_chars

            if len(words_in_line) == 1 or num_line == len(words):
                return " ".join(words_in_line) + " " * spaces

            num_words = len(words_in_line) - 1
            inbetween_base = spaces // num_words
            extra_spaces = spaces % num_words

            for j in range(extra_spaces):
                words_in_line[j] += " "

            for i in range(num_words):
                words_in_line[i] += " " * inbetween_base
            return " ".join(words_in_line)

        lines = []
        i = 0
        while i < len(words):
            curr = words_line(i)
            i += len(curr)
            lines.append(make_line(curr, i))
        return lines
