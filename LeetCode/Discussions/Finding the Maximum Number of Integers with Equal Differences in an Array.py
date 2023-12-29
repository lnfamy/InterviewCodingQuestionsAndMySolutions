"""
Link: https://leetcode.com/discuss/interview-question/4471415/Microsoft-OA
There is an array A made of N integers. Your task is to choose as many integers from A as possible so that, when they are put in ascending order, all of the differences between all pairs of consecutive integers are equal. For example, for A = [4, 3, 5, 1, 4, 4], you could choose 1, 3, and 5 (with differences equal to 2) or 4, 4, and 4 (with differences equal to 0). So, answer in this case will be 3.
What is the maximum number of integers that can be chosen? Write a function.

Example 1 :
A = [4, 7, 1, 5, 3], function should return 4. 4 integers (7, 1, 5, 3) when put in ascending order the difference between all consecutive integers is 2.

Example 2 :
A = [12, 12, 12, 15, 10], function should return 3. It is optimal to chose all 3 integers with value 12.

Example 3 :
A = [18, 26, 18, 24, 24, 20, 22], function should return 5. 5 integers (18, 20, 22, 24, 26) when put in ascending order the difference between all consecutive integers is 2. Notice that we cannot pick any other integers, even though they occur more than once.
"""


# BingChat solution
"""
This function takes an array A of integers as input and returns the maximum number of integers that can be chosen from A such that the differences between all pairs of consecutive integers are equal when they are put in ascending order.
The function first sorts the array A in ascending order. Then, it iterates through the sorted array and for each element, it calculates the difference between the current element and the next element. It then iterates through the rest of the array and counts the number of elements that have the same difference with their previous element. The maximum count is updated accordingly. Finally, the function returns the maximum count.
"""
def max_chosen_integers(A):
    n = len(A)
    A.sort()
    max_count = 1
    for i in range(n):
        count = 1
        diff = A[i + 1] - A[i]
        for j in range(i + 1, n):
            if A[j] - A[j - 1] == diff:
                count += 1
            else:
                break
        max_count = max(max_count, count)
    return max_count