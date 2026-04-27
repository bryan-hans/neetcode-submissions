class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 1 
        current = 1 

        nums = sorted(set(nums))

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current += 1 
                longest = max(current, longest)
            else:
                current = 1 
        
        return longest
        