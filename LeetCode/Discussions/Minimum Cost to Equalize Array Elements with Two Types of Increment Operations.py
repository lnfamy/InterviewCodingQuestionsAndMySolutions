"""
There is an array A of N integers and two types of operations that can be performed on the elements of the array:

increment a single element of A, which costs C1;
increment two elements of A, which costs C2. The chosen elements need to be in different positions.

What is the minimum total cost operations that will make all elements of A equal? As the result may be large, return its last nine digits without leading zeros (in other words, return the result modulo 10^9).
Write a function:

int solution(vector &A, int C1, int C2):

that, given an array A of N integers and two integers C1 and C2, returns the minimum cost of equalizing the array (modulo 10^9).

Examples:

Given A = [1, 4], C1 = 15 and C2 = 3, the function should return 45. We may increment the first element three times.

Given A [2, 11, 11, 11, 12), C1=10 and C2=4, the function should return 54. We may perform the following operations:

increment the first and the second element using the second operation three times: A=[5,14,11,11,12];

increment the first and the third element using the second operation three times: A = [8, 14, 14, 11, 12];
increment the first and the fourth element using the second operation three times: A=[11,14,14,14,12];
increment the first and the fifth element using the second operation twice: A=[13,14,14,14,14];
increment the first element using the first operation once: A = [14, 14, 14, 14, 14].

Given A = [1000000, 2, 1, 2, 1000000], C1 = 10000 and C2=4000. the function should return 999998000. We may perform the following operations:
increment the second and the third element using the second operation 499,999 times: A = [1000000, 500001, 500000, 2, 1000000];
increment the third and the fourth element using the second operation 499,999 times: A = [1000000, 500001, 999999, 500001,1000000]:
increment the second and the fourth element using the second operation 499,999 times: A = [1000000, 1000000, 999999, 1000000,
Increment the third element using the first operation once: A = [1000000, 1000000, 1000000, 1000000, 1000000].
The total cost is equal to 49999940003+10000 = 5999998000 but it should be returned modulo 10^9,

"""

"""
This function takes an array A of integers, an integer C1 representing the cost of incrementing a single element of A, and an integer C2 representing the cost of incrementing two elements of A as input. It returns the minimum total cost of operations that will make all elements of A equal, modulo 10^9.

The function first sorts the array A in ascending order. Then, it iterates through the range of values from the minimum value in A to the maximum value in A, and for each value, it calculates the cost of incrementing the elements of A to make them equal to the current value using both types of operations. The minimum cost is updated accordingly. Finally, the function returns the minimum cost modulo 10^9.
"""

def solution(A, C1, C2):
    A.sort()
    max_value = A[-1]
    min_cost = float('inf')
    for target in range(A, max_value + 1):
        cost1 = 0
        cost2 = 0
        for a in A:
            if a < target:
                cost1 += (target - a) * C1
                cost2 += ((target - a) // 2) * C2 + ((target - a) % 2) * C1
            else:
                break
        min_cost = min(min_cost, cost1, cost2)
    return min_cost % (10**9)

if __name__ == '__main__':
    A = [1, 4]
    C1 = 15
    C2 = 3
    print(solution(A, C1, C2))  # 45

    A = [2, 11, 11, 11, 12]
    C1 = 10
    C2 = 4
    print(solution(A, C1, C2))  # 54

    A = [1000000, 2, 1, 2, 1000000]
    C1 = 10000
    C2 = 4000
    print(solution(A, C1, C2))  # 999998000

