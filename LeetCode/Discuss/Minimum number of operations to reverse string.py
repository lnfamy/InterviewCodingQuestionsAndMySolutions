"""
Web Services stores grayscale images as an array of white and black pixels.
The image is stored as a binary string where a white pixel is represented by "1".
and a black pixel is represented by "0". The reverse of the image is represented as the reverse of
this binary representation . For example, the reverse of "11010" is "01011".
They want to store the reverse of each image as a backup.
In order to reproduce the reverse from the original, the following operation
can be preformed any number of times: remove any character from the string and append it
to the end of the string, i.e, choose any pixel and shift it to the end of the string.

Given the binary representation of pixels denoted by image, find the minimum number of operations
needed to produce its reverse.
"""


def solution(s: str) -> int:
    n = len(s)

    # we're going to compare s to the reverse of s using two pointers,
    # and make note of all of the indices where s matches reverse s.
    res = 0
    j = n - 1
    for i in range(n):
        if s[i] == s[j]:
            res += 1
        j -= 1

    return n - res
