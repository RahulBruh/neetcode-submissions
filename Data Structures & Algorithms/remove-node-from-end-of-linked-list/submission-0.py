# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
        bruh = {0: ListNode(None)}
        curr = head
        bruh[0].next = curr
        track = 1
        while curr:
            bruh[track] = curr
            track += 1
            curr = curr.next
        bruh[track] = None

        remove = track - n

        bruh[remove - 1].next = bruh[remove + 1]

        return bruh[0].next