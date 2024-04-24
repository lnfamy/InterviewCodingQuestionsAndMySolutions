"""
Bert has a fascination for sequences, he found a very nice problem with natural number sequences.
He has a number n, which indirectly implies that he has an integer sequence of [1, 2, 3, ..., n - 1].
Now he asks ernie to remove the minimum amount of elements from this sequence, such that the product of all integers
in the resulting sequence becomes congruent to 1 mod n [i.e if product of the resultant sequence is p, then p % n is 1]

NOTE:
    For all practical purposes, consider the product of an empty sequence to be 1.
    If there are multiple solutions, return the lexicographically smallest one
    Return the array in increasing order only.

INPUT:
    An integer n will be given as the argument of the function that you need to complete.
"""


def find_sequence(n, mod):
    answer = []
    m = 1

    for i in range(1, n):
        if i % mod:
            answer.append(i)
            m *= i % mod
            m %= mod

    if m == 1:
        return answer

    x = len(answer) - 1

    for i in range(x, -1, -1):
        if answer[i] % mod == m:
            answer[i] = 0
            break

    return [x for x in answer if x]


if __name__ == '__main__':
    N = int(input("Enter the value of N: "))
    MOD = int(input("Enter the value of mod: "))
    result = find_sequence(N, MOD)
    print("Resulting sequence:", result)
