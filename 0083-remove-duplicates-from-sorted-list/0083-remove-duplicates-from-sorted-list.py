# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicated_dic = {}
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        i = 0

        while curr.next:
            if curr.next.val in duplicated_dic:
                curr.next = curr.next.next
            else:
                duplicated_dic[curr.next.val] = curr.next.val
                curr = curr.next

        return dummy.next
        