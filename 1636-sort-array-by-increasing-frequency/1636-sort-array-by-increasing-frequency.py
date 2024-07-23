from collections import Counter
class Solution:
    """
        1.Count the frequency
        2.Sort based on frequency use values
        3.If there are same amount of frequency add them in decreasing order
        4.print the keys that goes with the values
     """
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
        