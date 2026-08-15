class Solution:
    def climbStairs(self, n: int) -> int:
        # initialzing last step (two) and second last step (one) as 1
        # result at each step depends on the result from next two steps, so we use bottom-up approach
        # Storing (caching) the result for less computation -> memoization

        one, two = 1, 1

        for i in range(n-1):
            result = one + two
            two = one
            one = result
        
        return one