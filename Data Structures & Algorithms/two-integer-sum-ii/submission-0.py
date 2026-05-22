class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = {}

        for i, n1 in enumerate(numbers):
            n2 = target - n1
            if n2 in ans:
                return [ans[n2] + 1, i + 1]
            ans[n1] = i 