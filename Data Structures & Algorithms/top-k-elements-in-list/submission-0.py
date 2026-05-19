class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  # count of element : [elements]
        # creating list of arrays, size of list = size of nums
        freq = [[] for i in range(len(nums) + 1)]  

        for num in nums:
            count[num] = 1 + count.get(num , 0)  # count 1->1, count 2->2, ...

        for num, c in count.items():
            freq[c].append(num)

        ans = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans