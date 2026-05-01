class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0 
        end = len(heights) - 1 
        res = 0

        while start < end:
            area = (end - start) * min(heights[start], heights[end])
            res = max(area, res)
            
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1
        
        return res