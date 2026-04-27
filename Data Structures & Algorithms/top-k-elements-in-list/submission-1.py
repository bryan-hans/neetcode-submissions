class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        each_number = {}

        for num in nums:
            if num not in each_number:
                each_number[num] = 1
            else:
                each_number[num] += 1
        
        sorted_numbers = sorted(each_number, key = each_number.get, reverse = True)

        return sorted_numbers[:k]

        