class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1 

        zero_count = nums.count(0)

        for num in nums:
            if num != 0:
                total_product *= num

        results = []

        for num in nums:
            if zero_count > 1: 
                results.append(0)
            elif zero_count == 1:
                if num == 0: 
                    results.append(total_product)
                else:
                    results.append(0)
            else:
                results.append(total_product // num)
        
        return results
        


        