class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        end = len(sorted_nums) - 1 
        res = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and num == sorted_nums[i -1]:
                continue
            start = i + 1 
            end = len(sorted_nums) - 1 
            while start < end:
                three_sum = num + sorted_nums[start] + sorted_nums[end]
                if three_sum == 0:
                    res.append([num, sorted_nums[start], sorted_nums[end]])
                    start += 1
                    end -= 1
                    while start < end and sorted_nums[start] == sorted_nums[start - 1]:
                        start += 1
                    while start < end and sorted_nums[end] == sorted_nums[end + 1]:
                        end -= 1
                elif three_sum > 0: 
                    end -= 1
                else:
                    start += 1 
        
        return res
