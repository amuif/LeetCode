class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split(" ")
        sorted_array = sorted(splitted, key = lambda x: x)
        splitted.sort(key = lambda x:x[-1])
        removed = [word[:-1] for word in splitted]
        output = ""
        for i in removed:
            output += i + " " 
        return output.strip()


        