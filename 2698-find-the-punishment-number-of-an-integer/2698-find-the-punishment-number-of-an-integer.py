class Solution:
    def punishmentNumber(self, n: int) -> int:
        output = 0

        def can_partition(sq_str, target, idx=0, current=0):
            """ Check if sq_str can be partitioned to sum to target """
            if idx == len(sq_str):
                return current == target  # If we reached end, check sum
            
            for j in range(idx + 1, len(sq_str) + 1):  # Try all splits
                part = int(sq_str[idx:j])  # Convert substring to number
                if can_partition(sq_str, target, j, current + part):
                    return True
            
            return False

        punishment = 0

        for i in range(1, n + 1):
            squared = i * i
            if can_partition(str(squared), i):
                punishment += squared

        return punishment

