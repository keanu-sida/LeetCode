# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.

# Return the length longest chain which can be formed.

# You do not need to use up all the given intervals. You can select pairs in any order.

 

# Example 1:

# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].
# Example 2:

# Input: pairs = [[1,2],[7,8],[4,5]]
# Output: 3
# Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
 

# Constraints:

# n == pairs.length
# 1 <= n <= 1000
# -1000 <= lefti < righti <= 1000

from typing import List
from math import inf

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:      # the pairs list is a list of lists of type integer
        pairs.sort(key=lambda x: x[1])                              # a lambda function is used as the key for sorting the pairs array
        curent_end, counter = float(-inf), 0                        # the current end of the chain and counter are each initialized here
        for pair in pairs:                                          # a for look is used to iterate over the ordered sequence of pairs
            if current_end < pair[0]:                               # if the current end to the chain (initialized to negative infinity) is less than the end of the next iteration,
                current_end = pair[1]                               # then we add it to the chain and make the new end the right side of the pair
                counter += 1                                        # we then increment the counter to track the length of our chain

        return counter                                              # finally, the function returns the total length after iterations are complete