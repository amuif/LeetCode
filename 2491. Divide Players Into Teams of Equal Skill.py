class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
      
        target_sum = skill[0] + skill[-1]
      
        left, right = 0, len(skill) - 1
      
        cumulative_product = 0
      
        while left < right:
            if skill[left] + skill[right] != target_sum:
                return -1
          
            cumulative_product += skill[left] * skill[right]
          
            left += 1
            right -= 1
      
        return cumulative_product
