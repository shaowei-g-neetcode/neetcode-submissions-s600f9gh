# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        first = head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        second = prev
        
        while second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            second = secondNext
            first = firstNext
    
