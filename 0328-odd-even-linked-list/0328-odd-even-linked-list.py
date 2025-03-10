# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        even_head = even_tail = ListNode(0)
        odd_head = odd_tail = ListNode(0)
        curr = head
        i = 1

        while curr:
            if i % 2 == 0:
                even_tail.next = curr
                even_tail = even_tail.next
            else:
                odd_tail.next = curr
                odd_tail = odd_tail.next
            i += 1
            curr = curr.next

        even_tail.next = None
        odd_tail.next = even_head.next
        return odd_head.next
