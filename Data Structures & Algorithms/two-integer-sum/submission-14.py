class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in differences:
                return [differences[diff], i]
            else:
                differences[num] = i 

            