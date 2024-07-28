class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        zipped = tuple(zip_longest(word1,word2,fillvalue=""))
        output = []
        print(zipped)
        for i in zipped:
           
            output.append(i[0])
            output.append(i[1])
        print(output)
        return "".join(output)
        