class Solution:
    def trap(self, height) -> int:
        amount = 0
        prefix = [0] * (len(height) + 1)
        suffix = [0] * (len(height) + 1)
        for i in range(len(height)):
            prefix[i] = max(prefix[i-1], height[i])
            suffix[len(height) - 1 - i] = max(suffix[len(height) - i], height[len(height) - 1 - i])

        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            amount += water

        return amount