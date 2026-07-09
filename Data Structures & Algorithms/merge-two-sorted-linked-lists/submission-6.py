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

        curr1 = list1
        curr2 = list2

        if not curr1: # if list1 is empty, return list2; vice versa
            return curr2
        if not curr2:
            return curr1

        # find the head of the merged list (min val)
        if curr1.val <= curr2.val:
            head = curr1
            curr1 = curr1.next
        else:
            head = curr2
            curr2 = curr2.next
        tail = head   # tail is where to attach the next node

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next

        # Attach the rest (one list is now empty)
        tail.next = curr1 if curr1 else curr2

        return head
