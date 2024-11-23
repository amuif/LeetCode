class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counted = Counter(nums1)
        counted1 = Counter(nums2)
        output = []

        for i in counted.keys():
            if i in counted1.keys():
                print(i)
                print(min(counted[i], counted1[i]))
                current = [i] * min(counted[i], counted1[i])
                output += current

        return output
