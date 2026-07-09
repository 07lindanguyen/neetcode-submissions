# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        # checks before each iteration, so stops when curr == None
        while curr != None:
            # Store the next node before we change the current node's next pointer
            # to  maintain a tether to the original path of advancement
            nextNode = curr.next
            # Reverse the current node's next pointer
            curr.next = prev
            # Move the previous and current pointers one step forward
            prev = curr
            curr = nextNode
        # When the loop ends, 'prev' and nextNode will be pointing to the new head
        return prev

