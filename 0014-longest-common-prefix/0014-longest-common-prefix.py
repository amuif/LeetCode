class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        x = zip(*strs)
        for i in x:
            if len(set(i)) == 1:
                output += i[0]
            else:
                break

        return output
