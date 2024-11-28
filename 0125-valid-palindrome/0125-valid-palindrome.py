class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""

        for i in s.lower():
            if i.isalnum():
                palindrome += i
        return palindrome == palindrome[::-1]