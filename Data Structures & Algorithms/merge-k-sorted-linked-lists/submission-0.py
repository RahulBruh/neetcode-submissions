from collections import defaultdict
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hashmap = defaultdict(list)
    
        lowest = 10**4
        highest = 0

        for v in lists:
            while v:
                lowest = v.val if v.val < lowest else lowest
                highest = v.val if v.val > highest else highest
                hashmap[v.val].append(v)
                v = v.next

        dummyhead = ListNode(0)
        curr = dummyhead

        for i in range(lowest, highest + 1):
            if i in hashmap:
                for n in hashmap[i]:
                    curr.next = n
                    curr = curr.next
            else:
                pass

        return dummyhead.next
        
