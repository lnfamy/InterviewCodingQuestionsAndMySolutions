"""
https://leetcode.com/problems/flipping-an-image/description/
"""
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def flip(row):
            reverse = []
            for element in image[row]:
                reverse = [element] + reverse
            return reverse

        # flipping each row
        for i in range(len(image)):
            image[i] = flip(i)

        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0

        return image
