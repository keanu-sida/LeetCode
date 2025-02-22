from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        n = len(s)
        i, stack = 0, []
        
        # iterate over length of string:
        while i < n:
            depth, val = 0, ''
            # if next character is -, increase depth per -
            while i < n and s[i] == '-':
                depth, i = depth + 1, i + 1
            # if next character isn't -, build value digit by digit
            while i < n and s[i] != '-':
                val, i = val + s[i], i + 1
            # if there is a stack, cull until only the parents of current node remain
            while stack and len(stack) > depth:
                stack.pop()
            # create a new node with the current value typecast to an integer
            node = TreeNode(int(val))
            # assuming there is a stack, assign node to its parent starting with left
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            # append current node to stack to ensure subsequent nodes are attached to it
            stack.append(node)

        return stack[0]
    
    '''
    Time complexity: O(n) since we are are building the stack with strictly increasing index.

    Space complexity: O(n) since we are creating a stack of at most n elements (i.e. if the tree is all left nodes)
    '''