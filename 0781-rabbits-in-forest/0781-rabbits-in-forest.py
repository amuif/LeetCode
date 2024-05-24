from collections import Counter
import math
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_counter = Counter(answers)
      
        total_rabbits = 0
      
        for number_of_other_rabbits, count in answer_counter.items():
            group_size = number_of_other_rabbits + 1
          
            number_of_groups = math.ceil(count / group_size)
          
         
            total_rabbits += number_of_groups * group_size
      
        return total_rabbits