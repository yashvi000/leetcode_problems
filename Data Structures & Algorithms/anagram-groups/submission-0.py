class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) # hash map of string: [anagrams of the hash map]

        for n in strs:
            count = [0]*26  # [a-z]

            for char in n:
                count[ord(char) - ord("a")] += 1  # a->0, ... , z->25
            group[tuple(count)].append(n)

        return list(group.values()) 