class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #index 0 = 1 
        #2 * 4 * 6 = 48 
        #index 1 = 2 
        #1 * 4 * 6 = 24 
        #1 * 2 * 4 * 6 = 48 
        # 48 / 2 = 24 
        # 48 / 1 = 48 
        #index 2 = 4 
        #1 * 2 * 6 = 12 
        #48 / 4 = 12 
        #error from dividing with 0
        #variable to count the amount of 0s 

        #if theres more then one zero, then everything is 0 
        result = []
        length = len(nums)
        total_product = 1 
        product = []

        zero_count = nums.count(0)

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


            

