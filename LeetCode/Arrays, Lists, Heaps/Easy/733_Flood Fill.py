"""
https://leetcode.com/problems/flood-fill/description/
"""


class Solution:
    """
    this is a 2d array. we can do this with recursion.
    the method fills one cell each time, at the end (after recursive call)
    recursive call calls for all adjacent cells.
    if a given sr, sc is out of bounds, do nothing and return
    else, color it to the given color

    the recursion will be of dfs logic
    """

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> \
            List[List[int]]:
        init_color = image[sr][sc]

        # using an inner function to execute the recursion
        def flood(sr, sc):
            # checking if we're out of bounds
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
                return
            # checking if this cell is already the target color, or if it's different than the original
            # cells color and therefore should not be filled
            if image[sr][sc] == color or image[sr][sc] != init_color:
                return

            image[sr][sc] = color

            flood(sr - 1, sc)
            flood(sr + 1, sc)
            flood(sr, sc - 1)
            flood(sr, sc + 1)

        flood(sr, sc)
        return image
