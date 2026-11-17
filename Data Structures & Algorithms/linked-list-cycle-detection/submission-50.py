# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = j = head

        if i.next == None:
            return False

        while i.next:
            i = i.next
            if j.next:
                j = j.next.next 
            if i == j:
                return True
        
        return False
            
