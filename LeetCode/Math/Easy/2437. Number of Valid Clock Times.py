"""
https://leetcode.com/problems/number-of-valid-clock-times/description/
"""
class Solution(object):
    def countTime(self, time):
        """
        :type time: str
        :rtype: int
        """
        sum_left = 0
        sum_right = 0

        if time[0] == time[1] == "?":
            sum_left += 24
        elif time[0] == "?":
            if int(time[1]) > 3:
                sum_left += 2
            else:
                sum_left += 3
        elif time[1] == "?":
            if int(time[0]) > 1:
                sum_left += 4
            else:
                sum_left += 10

        if time[3] == time[4] == "?":
            sum_right += 60
        elif time[3] == "?":
            sum_right += 6
        elif time[4] == "?":
            sum_right += 10

        if sum_left == 0 and sum_right != 0:
            return sum_right
        if sum_right == 0 and sum_left != 0:
            return sum_left
        if sum_right == sum_left == 0:
            return 1
        return sum_left * sum_right
