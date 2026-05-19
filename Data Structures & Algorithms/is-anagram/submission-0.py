class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Hash map solution
        s_hash, t_hash = {}, {}

        for i in range(len(s)):
            s_hash[s[i]] = s_hash.get(s[i], 0) + 1
            t_hash[t[i]] = t_hash.get(t[i], 0) + 1
        
        for char in s_hash:
            if s_hash[char] != t_hash.get(char, 0):
                return False
        
        return True