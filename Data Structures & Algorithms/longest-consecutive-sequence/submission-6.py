class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current = 1 
        longest = 1 

        if len(nums) == 0:
            return 0
        
        sorted_nums = sorted(set(nums))

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                current += 1 
                longest = max(current, longest)
            else:
                current = 1
        
        return longest
