class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        total_product = 1 
        results = []

        if zero_count > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                total_product *= num
        
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    results.append(total_product)
                else:
                    results.append(0)
            else:
                results.append(total_product // num)

        return results
