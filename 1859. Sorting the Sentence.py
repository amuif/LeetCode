class Solution:
    def sortSentence(self, s: str) -> str:
        listed = s.split()
        listed.sort(key=lambda x: x[-1])
        listed = [word[:-1] for word in listed]
        return " ".join(listed)
       
