class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert nums to a set for O(1) lookup
        num_set = set(nums)
        
        # Create a dummy node to handle edge cases where the head itself needs to be removed
        dummy = ListNode(0)
        dummy.next = head
        
        # Corrected: Two pointers - prev starts at dummy, and current starts at head
        prev, current = dummy, head
        
        while current:
            if current.val in num_set:
                # Skip the current node by linking prev to current.next
                prev.next = current.next
            else:
                # Move prev to current if current is not removed
                prev = current
            # Move to the next node in the list
            current = current.next
        
        # Return the new head (which is dummy.next)
        return dummy.next
