# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: empty list or single node
        if head == None or head.next == None:
            return head
        
        # Reverse the rest of the list
        newHead = self.reverseList(head.next)
        
        # Reverse current node's pointer
        # When we recursively go to the end of the list, 
        # that last node becomes the new head.
        head.next.next = head
        # set the original head's next to null to finish the reversal.
        head.next = None
        
        return newHead

