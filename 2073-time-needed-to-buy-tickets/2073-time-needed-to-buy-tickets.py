class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total_time = 0

        for index, tickets_at_this_position in enumerate(tickets):
            # If the current position is before or at the target position k
            if index <= k:
                # Add the minimum of the target tickets and tickets at the current position
                # It ensures we do not count the extra tickets the target person doesn't need
                total_time += min(tickets[k], tickets_at_this_position)
            else:
                
                total_time += min(tickets[k] - 1, tickets_at_this_position)
      
        # Return the calculated total time
        return total_time
        