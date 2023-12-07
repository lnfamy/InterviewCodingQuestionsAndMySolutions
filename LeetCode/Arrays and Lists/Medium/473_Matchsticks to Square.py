"""
https://leetcode.com/problems/matchsticks-to-square/
"""


class Solution:
    """
    approach: dynamic programming. i understand most of the idea, some of the things i dont understand
    """

    def makesquare_dynamic(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        l = len(matchsticks)
        perimeter = sum(matchsticks)
        # if the total perimeter constructed from all the matchsticks isn't divisible by 4,
        # then there is clearly no solution
        if perimeter % 4 != 0:
            return False

        quarter = perimeter // 4

        # memoization cache to prevent solving the same sub problem multiple times
        memo = {}

        def recursion(bit_mask, sides_done):
            total_used = 0
            # start: len(matchsticks) -1, stop: index -1 (not included, will stop at 0), step: -1
            for i in range(l - 1, -1, -1):
                if not bit_mask & (1 << i):
                    total_used += matchsticks[l - 1 - i]

            # if some of the matchsticks were used and the sum is divisible by our square's side,
            # increment sides completed by 1
            if total_used > 0 and total_used % quarter == 0:
                sides_done += 1

            if sides_done == 3:
                return True

            # if this sub problem has already been solved, return the stored value
            if (bit_mask, sides_done) in memo:
                return memo[(bit_mask, sides_done)]

            answer = False

            c = int(total_used // quarter)
            remaining = quarter * (c + 1) - total_used

            # iterate over all matchsticks
            for i in range(l - 1, -1, -1):
                # if the current matchstick can fit in the remaining space of the side and we havent
                # used it yet, try it
                if matchsticks[l - 1 - i] <= remaining and bit_mask & (1 << i):
                    if recursion(bit_mask ^ (1 << i), sides_done):
                        answer = True
                        break
            memo[(bit_mask, sides_done)] = answer
            return answer

        return recursion((1 << l) - 1, 0)

        # approach 2: recursion, depth first search
        def makesquare_dfs(self, matchsticks: List[int]) -> bool:
            if not matchsticks:
                return False

            l = len(matchsticks)
            perim = sum(matchsticks)
            if perim % 4 != 0:
                return False

            # reversing the matchstick list because we want to first consider the bigger ones
            matchsticks.sort(reverse=True)

            sums = [0] * 4

            def depth_first_search(index):
                if index == l:
                    return sums[0] == sums[1] == sums[2] == perim // 4

                for i in range(4):
                    # if the current matchstick can fit in the current side we're examining:
                    if sums[i] + matchsticks[index] <= perim // 4:
                        # then we recurse, to continue on and 'accept' this matchsticks into this side
                        sums[i] += matchsticks[index]
                        if depth_first_search(index + 1):
                            return True

                        # before other recursions occurr, we reverse the effects of this recursion:
                        sums[i] -= matchsticks[index]
                return False

            return depth_first_search(0)
