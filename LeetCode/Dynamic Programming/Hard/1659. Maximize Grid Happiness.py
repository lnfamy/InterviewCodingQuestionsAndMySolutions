"""
https://leetcode.com/problems/maximize-grid-happiness/description/
"""


class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        EMPTY, INTROVERT, EXTROVERT = 0, 1, 2

        # happiness impact table
        happiness_impact = [
            [0, 0, 0],
            [0, -60, -10],
            [0, -10, 40]
        ]

        @lru_cache(maxsize=None)
        def dfs(pos: int, prev_row_state: int, intro: int, extro: int) -> int:
            # base case: all cells are filled, or no people remaining
            if pos == m * n or (intro == extro == 0):
                return 0

            # no one is placed in the current cell
            max_happiness = 0

            # get the neighbor above value from the prev row state
            up = prev_row_state // pow(3, n - 1)
            left = 0 if pos % n == 0 else prev_row_state % 3

            for person in [EMPTY, INTROVERT, EXTROVERT]:
                # if not enough people of a type
                if (person == INTROVERT and intro == 0) or (person == EXTROVERT and extro == 0):
                    continue
                new_state = ((prev_row_state % pow(3, n - 1)) * 3) + person
                # happiness impact where up is 0, 1, or 2 (so empty, intro, extro) and so is person -
                # and this calculates the effect of the neighbor above on this person in terms of happiness
                # as shown in the table above
                additivehappiness = happiness_impact[up][person] + happiness_impact[left][person]
                resultanthappiness = dfs(pos + 1, new_state, intro - (person == INTROVERT),
                                         extro - (person == EXTROVERT))

                base_happy = 0
                if person == INTROVERT:
                    base_happy = 120
                elif person == EXTROVERT:
                    base_happy = 40

                # calculate total happiness
                total = additivehappiness + resultanthappiness + base_happy
                max_happiness = max(max_happiness, total)

            return max_happiness

        return dfs(0, 0, introvertsCount, extrovertsCount)
