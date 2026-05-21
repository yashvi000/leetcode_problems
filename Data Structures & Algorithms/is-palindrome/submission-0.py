class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new += i
        new = new.lower()

        if new == new[::-1]:
            return True
        return False