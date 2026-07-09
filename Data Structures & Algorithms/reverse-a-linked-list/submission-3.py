# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            # Store the next node before we change the current node's next pointer
            next_node = curr.next
            # Reverse the current node's next pointer
            curr.next = prev
            # Move the previous and current pointers one step forward
            prev = curr
            curr = next_node
        # When the loop ends, 'prev' will be pointing to the new head
        return prev

