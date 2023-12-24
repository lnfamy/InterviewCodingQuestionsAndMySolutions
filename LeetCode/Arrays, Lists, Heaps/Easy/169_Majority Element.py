"""
https://leetcode.com/problems/majority-element/description/
"""


class Solution:
    """
    approach 1: hashmap/dictionary
    while this approach works for the O(n) runtime requirement, it does not for the O(1) space requirement

    def majorityElement_v1(self, nums: List[int]) -> int:
        #create a default dictionary/hashmap structure where the default value for a key is 0
        keys = collections.defaultdict(int)

        #count every element in nums' number of occurrences
        for i in range(len(nums)):
            keys[nums[i]] += 1

        length = len(nums) / 2
        #iterate keys AND values using method keys.items() and a double parameter for loop
        for key, value in keys.items():
            if value > length:
                return key
        #if we got here, there's no such value
        return 0
    """
    """
    approach 2: brute force
    worth noting is that this solution, despite working on the exact same principle as the editorial
    brute force approach, will not compile when submitted because it exceeds the time limit. 
    this is because this solution has a worst case runtime of O(n^2), and we are looking for O(n), and also because
    python is much slower than say, java


    def majorityElement_v2(self, nums: List[int]) -> int:
        #define the max limit
        majority = len(nums) / 2
        for i in nums:
            count = sum(1 for j in nums if j == j)
            if count > majority:
                return i

    """
    """
    approach 3: sorting the array
    if the elements are sorted in a monotonous order, decreasing or increasing, because of the nature of this question
    where we are guaranteed to have an element that appears more than n/2 times , it is guaranteed to appear at 
    the middle of the array once we sort it

    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
    """

    """
    approach 4: bit manipulation
    if we were to represent the majority element, let's call it num, in bits 0 and 1, we could look at it this way:
    num appears more than n/2 times, therefore we could identify num by enumerating each bit to determine which value,
    0 or 1, is the majority for each bit placement. at the end we would convert the result back to integer value to get
    num.

    in python the sign of a number (positive or negative) is not representated using bits, therefore we have to make
    a special check when using python to determine the sign.
    all the numbers are in the range of int, so -10^10 to 10^9, so 32 bits. 

    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        #setting initial bit position
        bit = 1
        for i in range(31):
            #now we'll check how many numbers in num have this bit in this specific position, i/e this 'bit set'
            bit_count = sum(bool(num & bit) for num in nums)

            if bit_count > len(nums) / 2:
                majority += bit

            #shift current bit one space left, this is what we'll do for the whole thing
            bit = bit << 1

        #we'll count how many numbers are negative to see if the majority element is negative
        negative = sum(num < 0 for num in nums) > len(nums) / 2
        #now we add it all up
        if negative:
            majority -= bit

        return majority
    """

    """
    approach 5: randomization
    worst case is literal infinity though lol

    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) // 2
        while True:
            m = random.choice(nums)
            if sum(1 for element in nums if element == m) > n:
                return m
    """

    """
    approach 6: divide and conquer babey
    divide the array. if we know the majority element in the right half and the left half, we can determine
    which of them is the global majority in linear time. we'll utilize recursion
    """

    def majorityElement(self, nums: List[int], low=0, high=None) -> int:
        # make an inner function
        def majority_rec(low, high):
            # base case, exit condition: the array is of size 1
            if low == high:
                return nums[low]

            middle = (high - low) // 2 + low
            left = majority_rec(low, middle)
            right = majority_rec(middle + 1, high)

            # if both majority elements come out to be the same, thats the overall majority elements
            if left == right:
                return left

            # otherwise, we'll count appearances for each of them and determine like that
            l_count = sum(1 for i in range(low, high + 1) if nums[i] == left)
            r_count = sum(1 for i in range(low, high + 1) if nums[i] == right)

            if l_count > r_count:
                return left
            else:
                return right

        return majority_rec(0, len(nums) - 1)
