# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        right = dummy
        count = 0 

        # right pointer
        while count < n:
            right = right.next
            count +=1
        
        left = dummy
        # left pointer
        while right.next:
            left = left.next
            right = right.next

        left.next = left.next.next
        
        return dummy.next

