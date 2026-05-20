class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)
        pre, post = [nums[0]]*len(nums), [nums[-1]]*len(nums)

        for i in range(1, len(nums)):      # [0] = 1, [1] = 1*2, [2] = 2*3, [3] = 6*4
            pre[i] = pre[i-1] * nums[i]    # [1, 2, 6, 24]

        for i in range(len(nums)-2, 0, -1): # [3] = 4, [2] = 4*3, [1] = 12*2, [0] = 24*1
            post[i] = post[i+1] * nums[i]   # [24, 24, 12, 4]

        for i in range(len(nums)):           # [0]= 1*24, [1]= 1*12, [2]= 2*4, [3]= 6*1
            if i-1 in range(len(nums)):
                x = pre[i-1] 
            else: 
                x = 1
            
            if i+1 in range(len(nums)):
                y = post[i+1]
            else: 
                y = 1
            
            answer[i] = x * y                   # [24, 12, 8, 6]
        
        return answer