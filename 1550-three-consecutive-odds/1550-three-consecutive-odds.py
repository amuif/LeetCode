class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        for i in range(1,len(arr) - 1):
            if arr[i - 1] % 2 != 0 and arr[i] % 2 != 0 and arr[i + 1] % 2 != 0:
                print(i)
                print(arr[i-1],arr[i],arr[i+1])
                return True
        return False
