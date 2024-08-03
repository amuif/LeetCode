class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counted1 = Counter(target)
        counted2 = Counter(arr)

        return counted1 == counted2