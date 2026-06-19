class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0 
        end = len(numbers) - 1 

        while start < end:
            two_sum = numbers[start] + numbers[end]
            if two_sum == target:
                return [start + 1, end + 1]
            elif two_sum < target:
                start += 1 
            elif two_sum > target:
                end -= 1
            
        