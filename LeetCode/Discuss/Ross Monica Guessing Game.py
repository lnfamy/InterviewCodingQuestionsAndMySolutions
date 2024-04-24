"""
Ross has a number T = X + 0.5 where X is an integer btw 0 and N (inclusive). Monica attempts to guess this number by
asking one question: “Is i greater than or lesser than your number?” for some integer i btw 1 and N (inclusive). Ross
responds to Monica’s question by drawing a > (greater than) or < (lesser than) sign on the quiz board.

Monica being the competitive person that she is, comes up with a strategy to guess Ross’ number. Before making any
guesses, she creates a list of N numbers, where every number from 1 to N occurs exactly once in any order. Then she
goes through the list one by one, in the exact same order. But she skips any unnecessary guesses. That is, if the
number she’s about to guess is i and she had previously guessed some j < i and Ross told her it was greater than T,
then she would skip over i. Using this strategy, Monica is always able to accurately determine i, regardless of the
list she creates.

Ross hasn’t determined the value of T but he knows the list of numbers Monica is about to use.

Help Ross find the number of times he’ll draw a < (lesser than) sign immediately after drawing a > (greater than) sign
on the quiz board for each possible value of X where T = X + 0.5.
"""


def solution(v):
    n = len(v)
    d = [0] * (n + 2)
    have = {0: 0, n + 1: 0}

    for x in v:
        be = max(k for k in have.keys() if k < x)
        org = have[be]
        del have[be]

        if be < x:
            have[be] = 1

        have[x] = -1

        if org == 1:
            d[x] += 1
            d[be + 1] -= 1

    for i in range(1, n + 1):
        d[i] += d[i - 1]

    d.pop()
    return d


def main():
    print(solution([5, 1, 2, 4, 3, 6]))


if __name__ == "__main__":
    main()

"""
extra solution (asked chat to change variable names and make them more readable

def find_greater_counts(nums):
    n = len(nums)
    greater_counts = [0] * (n + 2)
    interval_status = {0: 0, n + 1: 0}
    
    for num in nums:
        previous_num = max(k for k in interval_status.keys() if k < num)
        previous_status = interval_status[previous_num]
        del interval_status[previous_num]
        
        if previous_num < num:
            interval_status[previous_num] = 1
        
        interval_status[num] = -1
        
        if previous_status == 1:
            greater_counts[num] += 1
            greater_counts[previous_num + 1] -= 1
    
    for i in range(1, n + 1):
        greater_counts[i] += greater_counts[i - 1]
    
    greater_counts.pop()
    return greater_counts

def main():
    numbers = [5, 1, 2, 4, 3, 6]
    result = find_greater_counts(numbers)
    print(result)

if __name__ == "__main__":
    main()


and explanation:
Certainly! Let's go through the variables and their roles in the code:

1. `nums`: This variable represents the list of numbers Monica is about to use to guess Ross's number. It's the input
to the `find_greater_counts` function.

2. `n`: Represents the length of the list `nums`, indicating the total number of numbers Monica is using.

3. `greater_counts`: This list stores the count of '>' signs immediately followed by a '<' sign for each possible 
value of X. Each element `greater_counts[i]` represents the count of such occurrences for the number X = i - 1.

4. `interval_status`: This dictionary keeps track of the status of each interval between the numbers Monica has 
guessed. The keys represent the starting points of the intervals, and the values represent the status of the 
intervals ('>', '<', or 0).

5. `num`: Represents the current number being processed in the loop. It's one of the numbers Monica is using to guess 
Ross's number.

6. `previous_num`: Stores the largest number less than `num` that Monica has guessed previously. It helps in 
determining the status of the interval between `previous_num` and `num`.

7. `previous_status`: Represents the status of the interval between `previous_num` and `num`. It indicates whether 
Monica previously received a '>' sign for this interval.

These variables collectively help in implementing the strategy described in the problem statement, where Monica skips 
unnecessary guesses and accurately determines Ross's number.

"""