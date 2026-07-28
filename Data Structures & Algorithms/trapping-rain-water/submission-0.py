class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0

        for i in range(1, len(height) - 1):
            left_max = max(height[:i])
            right_max = max(height[i + 1:])

            trapped = min(left_max, right_max) - height[i]

            if trapped > 0:
                total += trapped

        return total