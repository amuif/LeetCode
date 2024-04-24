class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # find the unique number
        mapper = Counter(nums)
        unique = list(mapper.keys())
        unique.sort(reverse = True)
        
        count = 0
        next_count = 0
        for i in range(1, len(unique)):
            one = mapper[unique[i - 1]] + next_count
            count += one
            next_count = one
        
        return count
