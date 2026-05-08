class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r :
            middle = (l + r) // 2
            if nums[middle] > nums[r]:
                l = middle + 1 
            else:
                r = middle
        
        min_index = l

        if min_index == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_index - 1]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, len(nums) - 1
        
        while l <= r:
            middle = (l + r) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1 
        
        return -1
    