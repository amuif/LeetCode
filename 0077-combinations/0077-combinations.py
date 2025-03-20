class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(group,now):
            if len(group) == k:
                ans.append(group[:])
                return 

            for i in range(now,n+1):
                group.append(i)
                backtrack(group,i+1)
                group.pop()

        backtrack([],1)
        return ans
    

        