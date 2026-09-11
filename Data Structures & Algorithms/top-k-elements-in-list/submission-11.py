class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}

        for num in nums:
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1 
        
        sorted_freq = sorted(num_count, key = num_count.get, reverse = True)
        return sorted_freq[:k]
        





        