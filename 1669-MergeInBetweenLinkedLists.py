### You are given two linked lists: list1 and list2 of sizes n and m respectively.

### Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

### Build the result list and return its head.

# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # initialize pointer to get to pth element
        ptr = list1
        for _ in range(a-1):
            ptr = ptr.next

        # initialize pointer to get to qth element
        qtr = ptr.next
        for _ in range (b - a + 1):
            qtr = qtr.next

        # add new list to ptr
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        
        # tag end of list1 onto end
        list2.next = qtr

        return list1