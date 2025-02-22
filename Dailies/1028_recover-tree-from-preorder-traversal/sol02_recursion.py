from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.index = 0
    
    def recoverFromPreorder(self, traversal: str) -> TreeNode:
        return self.helper(traversal, 0)
    
    def helper(self, traversal, depth):
        if self.index >= len(traversal):
            return None

        # reset the dash count, then compute it for the next number in the sequence
        dash_count = 0
        while (
            self.index + dash_count < len(traversal)
            and traversal[self.index + dash_count] == '-'
        ):
            dash_count += 1
        
        # if the depth of the visited number is below that of the current recursion, skip
        if dash_count != depth:
            return None
        
        # otherwise, go to the value and extract it
        self.index += dash_count
        value = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            value = value * 10 + int(traversal[self.index])
            self.index += 1
        node = TreeNode(value)

        # recursively build the left and right subtrees to this node
        node.left = self.helper(traversal, depth + 1)
        node.left = self.helper(traversal, depth + 1)

        return node

'''
Time complexity: O(n) since the recursive element isn't starting from 0, rather the current index variable

Space complexity: O(n) since, in a fully skewed tree, the recursive call stack space will hold the entire tree.
'''