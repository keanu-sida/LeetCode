# Solution 1: Organic, no help apart from some syntax for implementing the for loop.
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = Counter(nums)
        total = len(nums)
        ans = []
        for key, value in freq.items():
            if value > (total / 3):
                ans.append(key)
        return ans
        
# Solution 2: Second implementation, with list comprehension:
class Solution(object):
    def majorityElement(self, nums):
        freq = Counter(nums)
        total = len(nums)
        freq_nums = [num for num, frequency in freq.items() if frequency > (total/3)]
        return freq_nums
    
# Solution 3: Optimized from solutions to run in linear space, utilizing a new algorithm: the Boyer-Moore Voting Algorithm. A picture of the general implementation is in the folder.
class Solution(object):
    def majorityElement(self, nums):
        cand1, cand2, count1, count2 = 0, 1, 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
            
        return [num for num in (cand1, cand2) if nums.count(num) > len(nums) // 3]