# Greedy approach:
from typing import List
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        arr = [0] * (n+1)                                           # initialize an empty array which shows 
        for i, r in enumerate(ranges):
            if r == 0:
                continue
            left = max(0, i - r)
            arr[left] = max(arr[left], i + r)

        end, far_can_reach, cnt = 0, 0, 0
        
        for i, reach in enumerate(arr):
            if i > end:
                if far_can_reach <=end:
                    return -1
                end, cnt = far_can_reach, cnt + 1
            far_can_reach = max(far_can_reach, reach)

        return cnt + (end < n)

# Dynamic programming approach:

class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i, r in enumerate(ranges):
            start, end = max(0, i - r), min(n, i + r)
            for j in range(start + 1, end + 1):
                dp[j] = min(dp[j], dp[start] + 1)
                
        return dp[-1] if dp[-1] != float('inf') else -1