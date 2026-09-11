class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        curr = 1
        longest = 1
        sorted_nums = sorted(nums)



        for index in range(1, len(sorted_nums)):
            if sorted_nums[index] == sorted_nums[index - 1]:
                continue
            if sorted_nums[index] == sorted_nums[index - 1] + 1:
                curr += 1 
                longest = max(curr, longest)
            else:
                curr = 1
        
        return longest
            





        