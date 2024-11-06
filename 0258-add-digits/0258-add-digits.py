class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        sumi = 0

        while num > 9:
            for i in str(num):
                sumi += int(i)
            if sumi < 9:
                return sumi
            num = sumi
            sumi = 0
        return sumi
