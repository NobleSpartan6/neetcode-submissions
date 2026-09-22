class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        # two pointers 
        i = 0
        j = len(heights) - 1
        
        while i < j: 
            current_area = min(heights[i], heights[j]) * (j - i)
            area = max(area, current_area)
            
            # update pointers to maximize height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return area