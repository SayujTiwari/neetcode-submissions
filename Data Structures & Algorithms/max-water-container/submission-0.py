class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amounts = []
        left =0 
        right = len(heights) - 1

        while left < right:
            small = min(heights[left], heights[right])
            amounts.append(small*(right-left))
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1

        return max(amounts)