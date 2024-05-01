class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            letter = word.index(ch)
            prefix = word[:letter+1][::-1]
            return prefix + word[letter+1: ]
        else:
            return word
       
        