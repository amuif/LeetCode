class Solution:
    def find(self,nums,guess):
      start = 0
      end = start + guess
      s = sum(nums[start:end])
      
      while end < len(nums):

        l = end - start
        if (l-s) <= 1:
          return s
        
        s-=nums[start]
        start+=1
        
        s+=nums[end]
        end+=1
      
      l = end - start
      if (l-s) <= 1:
        return s
      
      return -1

      
    def longestSubarray(self, nums: List[int]) -> int:
        
        lo = 0
        hi = len(nums)

        ans = 0

        while lo<=hi:
          mid = (lo+hi)//2
          possible = self.find(nums,mid)
          if possible != -1:
            ans = max(ans,mid-1)
            lo=mid+1
          else:
            hi=mid-1

        return ans