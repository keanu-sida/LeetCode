# 442. Find All Duplicates in an Array
### Given an integer array nums of length n where all integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appear twice.
### Must run in O(n) time and use constant extra space.

from typing import List, Optional



class Solution:
    # fxn will take in a list of ints & return a smaller one
    def findDuplicates(nums: List[int]) -> List[int]:
        # initalize empty array to store duplicate nums
        ans = []
        # iterate over each num in array
        for num in nums:
            # take absolute value of num, then check if using it as an index returns a negative value
            x = abs[num]
            # if it does, it has been seen once
            if nums[x - 1] < 0:
                ans.append(num)
            # if it doesn't, multiply it by -1 to "mark" it
            else:
                nums[x - 1] *= -1
        # return array of answers
        return ans