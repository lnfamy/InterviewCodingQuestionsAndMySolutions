"""
https://leetcode.com/problems/integer-to-roman/description/
"""


# approach: greedy
class Solution:
    def intToRoman(self, num: int) -> str:
        distincts = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                     (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                     (5, "V"), (4, "IV"), (1, "I")]

        res = []
        for val, rom in distincts:
            if num == 0:
                break
            count, num = divmod(num, val)
            res.append(rom * count)
        return "".join(res)

    def intToRoman_brute_force(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return "" + thousands[num // 1000] + hundreds[num % 1000 // 100] + tens[num % 100 // 10] + ones[num % 10]