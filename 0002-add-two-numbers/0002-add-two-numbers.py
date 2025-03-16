# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0
    ) -> Optional[ListNode]:
        if not l1 and not l2 and carry == 0:
            return None

        total = (l1.val if l1 else 0 )+( l2.val if l2 else 0 )+ carry

        carry = total // 10
        new_node = ListNode(total % 10)
        new_node.next = self.addTwoNumbers(l1.next if l1 else 0, l2.next if l2 else 0, carry)

        return new_node
