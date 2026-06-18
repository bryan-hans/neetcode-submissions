class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        product = 1 
        output = []

        if zero_count > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                product *= num

        for num in nums:
            if zero_count == 1: 
                if num == 0:
                    output.append(product)
                else:
                    output.append(0)
            else:
                output.append(product // num)
        
        return output
        
        
             
        
        