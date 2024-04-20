"""
https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
"""
import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        freq = collections.Counter(s)
        res_arr = {}

        res_arr["0"] = freq['z']
        res_arr["2"] = freq['w']
        res_arr["4"] = freq['u']
        res_arr["6"] = freq['x']
        res_arr["8"] = freq['g']
        res_arr["3"] = freq['h'] - res_arr["8"]
        res_arr["5"] = freq['f'] - res_arr["4"]
        res_arr["7"] = freq['s'] - res_arr["6"]
        res_arr["9"] = freq['i'] - res_arr["6"] - res_arr["8"] - res_arr["5"]
        res_arr["1"] = freq['o'] - res_arr["0"] - res_arr["2"] - res_arr["4"]

        output = [key * res_arr[key] for key in sorted(res_arr.keys())]
        return "".join(output)
