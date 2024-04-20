"""
Shopping online for some bags of onions. each listing displays the number of onions the bag contains.
I want to buy a perfect set of onion bags from the entire search results list - onionBags.
A perfect set of onion bags, named "perfect", is defined as such:
    1. The set contains at least two bags of onion
    2. When the onion bags in the perfect set sorted in increasing order by count of onions in each bag, the following
        conditions are met:
        1. for all 1 <= i < n, where n is the size of the set, perfect[i]*perfect[i] = perfect[i+1]

    find the largest possible perfect set and return an integer - the size of that set. if no such set is possible,
    return -1. it is guaranteed all elements in onionbags are distinct.
"""
from typing import List


def perfectSet(onionBags: List[int]) -> int:
    bags = set(onionBags)
    count = 1
    res = 0

    # going over in one pass
    for i in range(len(onionBags)):
        # setting the current bag to be checked as onionBags[i], so using the for loop we check
        # the max amount of items in a perfect set like this
        num = onionBags[i]
        # while there's a bag in the given list that satisfies the condition to making it onto the perfect set
        while num * num in bags:
            # increment the count of items in perfect set, and set num to the next bag we're checking
            count += 1
            num = num * num
            # count gets reset, so we can find the max option of it all
            res = max(count, res)
        # since count gets reset, and we check a different element in every for loop iteration, we reset count
        # to 1 after we finish checking an element's 'prospects'
        count = 1

    return res
