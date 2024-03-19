# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Solution 1: Dynammic Programming (Time O(n**2), Space O(n**2))

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]

        for i in range(1, numRows):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1]+prev_row[j])
            
            new_row.append(1)
            triangle.append(new_row)
        
        return triangle