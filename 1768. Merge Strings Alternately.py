class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []
        for i,j in zip_longest(word1,word2,fillvalue=""):
            output+=[i,j]
           

        return ''.join(output)
