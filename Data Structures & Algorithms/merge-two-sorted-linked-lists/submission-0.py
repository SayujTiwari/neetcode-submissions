# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        c1 = list1
        c2 = list2

        while c1 is not None and c2 is not None:
            if c1.val < c2.val:
                node.next = c1
                c1 = c1.next
            else:
                node.next = c2
                c2 = c2.next

            node = node.next

        if c1 is not None:
            node.next = c1
        else:
            node.next = c2

        return dummy.next




