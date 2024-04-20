class Solution:
    def smallestNumber(self, num: int) -> int:
        # lowest numbers
        if num < 0:
            nums = [ i for i in str(num) if i != '-']
            return -int(''.join(sorted(nums, reverse = True)))
        
        st = str(num)
        zeros = '0' * st.count('0')
        k = [i for i in st if i != '0']
        if k:
            k.sort()
            new = k[0] + zeros + ''.join(k[1:])
            return int(new)

        return 0
        