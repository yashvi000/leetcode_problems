class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        
        parentheses = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in parentheses:
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        else:
            return True