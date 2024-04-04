class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dic = {}
        # for num in zip(nums1,nums2):
        #     dic[num] =  dic.get(num, 0) + 1
        # print( dic )
        dic1 = {}
        dic2 = {}
        m =0
        i = 0
        output=[]
        for num in nums1:
            dic1[num] = 1 + dic1.get(num,0)
        for num in nums2:
            dic2[num] = 1 + dic2.get(num,0)
        print(dic1)
        print(dic2)
        # there should be a math to know the difference or min ()

        for key in dic1.keys():
            i +=1
            

            if key in dic2.keys():
                diff = min(dic1.get(key),dic2.get(key))
                print(diff)
                print(m)
                for num in range(diff):
                    output.append(key)
        return output        
