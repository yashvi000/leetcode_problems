class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [0]*len(height), [0]*len(height)
        total = 0

        for i in range(1, len(height)):
            max_l[i] = max(max_l[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            max_r[i] = max(max_r[i+1], height[i+1])

        for i in range(len(height)):
            h = min(max_l[i], max_r[i]) - height[i]
            if h >= 0:
                total += h

        return total