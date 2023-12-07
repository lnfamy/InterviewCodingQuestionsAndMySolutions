"""
https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/
"""
class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # solved alone using hint :D
        # runtime complexity is O(NlogN) bc the sort() function is a comparison based sorting algorithm
        # the rest of the code runs in linear time
        cost.sort()
        cost.reverse()
        count = 0
        total_cost = 0

        for candy in cost:
            if count == 2:
                count = 0
                candy = 0
            else:
                count += 1
            total_cost += candy

        return total_cost
