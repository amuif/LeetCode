from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # counted = Counter(arr1)
        mapper = Counter()
        for i in range(arr2.__len__()):
            mapper[arr2[i]] = i
        def c(x):
            return mapper[x] if x in mapper else x + 1000   
        output = sorted(arr1, key=lambda x: c(x))
        return output 
