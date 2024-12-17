class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = Counter(nums1)
        num2 = Counter(nums2)
        output = []

        for i in num1.keys():
            if i in num2.keys():
                result = [i] * min(num1[i], num2[i])
                output += result
        return output
        