# Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.
# The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.
# The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.
# Return an array of the k parts.

# Solution 1: Time O(n), Space O(k)

from typing import ListNode, Optional, List

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length, current, parts = 0, head, []
        
        while current:
            length += 1
            current = current.next
        
        base_size, extra = divmod(length, k)
        current = head
        
        for _ in range(k):
            dummy = ListNode()
            part_head = dummy
            
            for _ in range(base_size + (extra > 0)):
                dummy.next, current, dummy = current, current.next, current
            
            if extra > 0:
                extra -= 1
  
            dummy.next = None
            parts.append(part_head.next)
        
        return parts