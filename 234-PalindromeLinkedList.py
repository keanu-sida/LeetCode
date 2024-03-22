### Given the head of a singly linked list, return true if it is a palindrome.

# initialize list node class
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    # define is palindrome with optional , since fxn still works with empty arg
    def isPalindrome(head: Optional[ListNode]) -> bool:
        # initialize empty array to be used to remember each element
        vals = []

        # add each element in linked list to array
        while head:
            vals.append(head)
            head = head.next

        # initialize left and right pointers
        l, r = 0, len(vals) - 1

        # compare elements at opposite ends until elements dont match or pointers meet in the middle or
        while l < r and vals[l] == vals[r]:
            l += 1
            r -= 1

        # return true if left meets or goes one past right in the case of even length array
        return l >= r