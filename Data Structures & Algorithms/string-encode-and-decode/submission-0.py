class Solution:

    def encode(self, strs: List[str]) -> str:
        # encoded : ["abc", "xy"] -> "3#abc2#xy"
        ans = ""
        for x in strs:
            ans += str(len(x)) + "#" + x
        return ans

    def decode(self, s: str) -> List[str]:
        # decoded : "3#abc2#xy" -> ["abc", "xy"]
        ans = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])  # reads s[i] if s[i]= number and s[j]= "#" 
            ans.append(s[j+1 : j+1 + size])
            i = j + 1 + size  # next character after appending string of length = size
        
        return ans