# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode()
        bruh = dummy

        addresses = []

        curr = head

        while curr:
            addresses.append(curr)
            curr = curr.next

        l, r = 0, len(addresses) - 1

        while l < r:
            bruh.next = addresses[l]
            bruh = bruh.next
            bruh.next = addresses[r]
            bruh = bruh.next

            l += 1
            r -= 1
        
        if l == r:
            bruh.next = addresses[l]
            bruh = bruh.next
        
        bruh.next = None




