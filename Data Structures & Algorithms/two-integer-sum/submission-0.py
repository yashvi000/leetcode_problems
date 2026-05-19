class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # element : index

        for i, n1 in enumerate(nums):
            n2 = target - n1
            if n2 in hash_map:
                return [hash_map[n2], i]
            hash_map[n1] = i