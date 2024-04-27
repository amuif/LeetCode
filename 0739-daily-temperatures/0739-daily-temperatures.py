from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_temp = [(temperatures[-1], len(temperatures)-1)]
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)-2, -1, -1):
            while stack_temp and temperatures[i] >= stack_temp[-1][0]:
                stack_temp.pop()
            if stack_temp:
                ans[i] = stack_temp[-1][1] - i
            stack_temp.append((temperatures[i], i))

        return ans
