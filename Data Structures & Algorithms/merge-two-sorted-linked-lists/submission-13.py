# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # compare values
        # Create a sentinel node bc you're creating a new list (need somewhere to put nodes)

        sentinel = ListNode() # create a sentinel (standard method)
        tail = sentinel  # tail is where to attach the next node (will be tail)
        curr1 = list1 # actual node
        curr2 = list2
        # whichever is less, move their pointer (to indicate its been counted)
        while curr1 and curr2:
            if curr1.val <= curr2.val: # values of the nodes
                tail.next = curr1 
                curr1 = curr1.next
            else:
                tail.next = curr2 
                curr2 = curr2.next
            # tail traverses the merged list (last node in the merged lst)
            tail = tail.next
        # Attach the rest of one list if other is null/reaches null
        if curr1 is not None:
            tail.next = curr1 
        else:
            tail.next = curr2
        # Return the node after the sentinel (the head)
        return sentinel.next
