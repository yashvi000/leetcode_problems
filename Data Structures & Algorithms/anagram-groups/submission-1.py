class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list) # sorted string: [anagrams of the sorted string]

        for n in strs:
            sorted_str = "".join(sorted(n))
            group[sorted_str].append(n)

        return list(group.values())