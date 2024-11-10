class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sorting_array = []
        l = 0
        for i in arr2:
            for j in arr1:
                if j == i:
                    sorting_array.append(j)
        arr1.sort()
        for i in arr1:
            if i not in arr2:
                sorting_array.append(i)
        
        return sorting_array
