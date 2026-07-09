# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # compare each node from both lists simultaneously
        # since both are sorted; compare values
        # append by min-->max value

        # Create a sentinel node
        sentinel = ListNode()
        tail = sentinel  # tail is where to attach the next node

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        # Attach the rest (one list is now empty)
        if curr1 is not None:
            tail.next = curr1 
        else:
            tail.next = curr2

        # Return the node after the sentinel (the actual head)
        return sentinel.next
