class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hashi=defaultdict(int)
        goodPairs= 0

        for num in nums:
            hashi[num]+=1
        for key,val in hashi.items():
            if val==2:
                goodPairs +=1
            elif val >2:
                temp = (val*(val - 1))//2
                goodPairs += temp
        return goodPairs
    
     
