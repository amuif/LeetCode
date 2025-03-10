# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_tails = less_head = ListNode(0)
        greater_tails = greater_heads = ListNode(0)
        curr = head

        while curr:
            if curr.val < x:
                less_tails.next = curr
                less_tails = less_tails.next

            else:
                greater_tails.next = curr
                greater_tails = greater_tails.next

            curr = curr.next

        greater_tails.next = None 
        less_tails.next = greater_heads.next

        return less_head.next
