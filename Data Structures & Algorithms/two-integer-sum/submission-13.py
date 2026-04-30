class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        differences = {}

        for index, num in enumerate(nums):
            difference = target - num
            if difference in differences:
                return [differences[difference], index]
            else:
                differences[num] = index



        