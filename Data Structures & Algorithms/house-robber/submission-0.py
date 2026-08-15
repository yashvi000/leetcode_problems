class Solution:
    def rob(self, nums: List[int]) -> int:
        way_1 = 0   
        way_2 = 0   

        for n in nums:     # [..., way_1, way_2, n, ...]
            max_rob = max(way_1 + n, way_2)
            way_1 = way_2
            way_2 = max_rob
            
        return way_2