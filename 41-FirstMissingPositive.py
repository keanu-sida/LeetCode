# LC 41: First Missing Positive
### Given unsorted integer array nums, return the smallest positive integer not in nums.
### Must run in O(n) time and with O(1) auxiliary space.

# approach: create range element of length of list, 
        # then swap elemets with their corresponding index - 1
        # then iterate over the range element once more and return first element not swapped
        # if all elements swapped, return n + 1 since list is just all positive ordered integers

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:              
        # create small fxn to swap two elements in an array
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        n = len(nums)

        # Iterate over list, switching elements for their index - 1
        # Only do so if nums[i] > 0 since we only care about positive integers
        # Also qualify that nums[i] need be <= n since any number greater wont be relevant
        # to smallest omitted integer
        # Finally, ensure that nums[i] != nums[nums[i] - 1], since that means they are dupes.
        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)

        # Iterate over the range once more and find the first index that wasn't manipulated.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
    

    