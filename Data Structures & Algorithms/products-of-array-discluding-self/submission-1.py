class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        pre, post = 1, 1
                                        
        for i in range(len(nums)):      # nums = [1, 2, 3, 4]
            answer[i] = pre             # pre = 1 -> 1 -> 2 -> 6 -> 24
            pre *= nums[i]              # answer = [1, 1, 2, 6]

        for i in range(len(nums)-1, -1, -1): 
            answer[i] *= post           # post = 1 -> 4 -> 12 -> 24 -> 24
            post *= nums[i]             # answer[-1] = [6, 8, 12, 24]

        return answer                   # answer = [24, 12, 8, 6]