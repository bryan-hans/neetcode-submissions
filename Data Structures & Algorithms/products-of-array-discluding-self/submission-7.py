class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        length = len(nums)
        total_product = 1
        result = []

        if zero_count > 1:
            return [0] * length
        
        for num in nums:
            if num != 0:
                total_product *= num
        
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    result.append(total_product)
                else:
                    result.append(0)
            else:
                result.append(total_product // num)
        
        return result



            

