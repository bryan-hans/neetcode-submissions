class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        output = []

        if zero_count > 1:
            return [0] * len(nums)
        
        total_product = 1
        for num in nums:
            if num != 0:
                total_product *= num
        
        for num in nums:
            if zero_count == 1:
                if num == 0:
                    output.append(total_product)
                else:
                    output.append(0)
            else:
                output.append(total_product // num)
        return output
    




        
        

