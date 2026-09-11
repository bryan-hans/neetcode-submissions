class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d_count = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in d_count:
                return [d_count[difference], i]
            d_count[n] = i
