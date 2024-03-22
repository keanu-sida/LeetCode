# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition of singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
    
        return prev