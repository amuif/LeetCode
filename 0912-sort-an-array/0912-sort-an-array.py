class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left_part,right_part):
            output = []
            l = r = 0
            while l < len(left_part) and r < len(right_part):
                if left_part[l] > right_part[r]:
                    output.append(right_part[r])
                    r+=1
                else:
                    output.append(left_part[l])
                    l+=1
            if l < len(left_part):
                output.extend(left_part[l:])
            if r < len(left_part):
                output.extend(right_part[r:])

            return output
            
        
        def merge_sort(left,right):
            if left == right:
                return [nums[left]]

            middle = (right+left)//2
            sort_left = merge_sort(left,middle)
            sort_right = merge_sort(middle+1,right)
            return merge(sort_left,sort_right)

        return merge_sort(0,len(nums)-1)