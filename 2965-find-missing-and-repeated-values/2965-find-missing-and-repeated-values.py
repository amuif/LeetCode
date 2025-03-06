class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        output = []
        or_num = []
        my_num = list_1D = [item for sub_list in grid for item in sub_list]
        counted = Counter(my_num)
        for key,value in counted.items():
            if value == 2:
                output.append(key)
                or_num.extend([key,key])
            else:
                or_num.append(key)
        all_num = [num+1 for num in range(len(or_num))]

        for i in all_num:
            if i not in or_num:
                output.append(i)
        return output
