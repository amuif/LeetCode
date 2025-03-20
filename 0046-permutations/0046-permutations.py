class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        unique = set()
        path = []
        def backtrack(path,unique):
            if len(path) == n:
                ans.append(path[:])
                return ans

            for i in nums:
                if i in unique:
                    continue

                path.append(i)
                unique.add(i)

                backtrack(path,unique) 
                
                path.pop()
                unique.remove(i)

        backtrack(path,unique)
        return ans
        