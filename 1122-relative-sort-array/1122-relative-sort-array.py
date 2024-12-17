class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output = []
        arr1_counted = Counter(arr1)
        print(arr1_counted)
        not_in_arr2 = []

        for i in arr1:
            if i not in arr2:
                not_in_arr2.append(i)
        not_in_arr2.sort()

        for i in range(len(arr2)):
            count = arr1_counted.get(arr2[i], 0)
            output.append([arr2[i]] * count)
        flat = sum(output,[])

        return  flat + not_in_arr2