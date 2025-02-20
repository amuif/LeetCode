class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1 
        count = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]
            remainder = prefix_sum % k
            count += prefix_cnt[remainder]
            prefix_cnt[remainder] += 1


        return count

        