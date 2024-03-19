# A string s is called good if there are no two different characters in s that have the same frequency.
# Given a string s, return the minimum number of characters you need to delete to make s good.
# The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

## Initial first thoughts:
# We will need a hashmap to store frequencies of each letter.
# Next, we will iteratively create an array with each frequency to figure out if any is duplicated.
# Next, for duplicate element i, we will see if i + 1 or i - 1 is in n[i]. If soIf not, we will iterate our counter accordingly and change the indexed number in our array. We will then move on to the next number.

# First Attempt
# class Solution(object):
#     def minDeletions(self, s):
#         freq = {}
#         counter = 0
#         for char in s:
#             if (char in freq):
#                 freq[char] = freq[char] + 1
#             else:
#                 freq[char] = 1
        
        
#         print(freq)
#         return counter
    
# From here, unsure how to get frequencies alone from hashmap

# Solution 1:
from collections import Counter

class Solution:
    def minDeletions(s: str) -> int:
        cnt = Counter(s)
        deletions = 0
        used_frequencies = set()
        print(cnt.items())
        for char, freq in cnt.items():
            while freq > 0 and freq in used_frequencies:
                freq -= 1
                deletions += 1
            used_frequencies.add(freq)
            print(used_frequencies)
            
        return deletions
    
print(Solution.minDeletions('fasdfkwgnlsa'))
