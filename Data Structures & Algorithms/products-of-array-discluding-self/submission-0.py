class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        leftProd = 1

        right = [1] * len(nums)
        rightProd = 1

        for i in range(len(nums)):
            left.append(leftProd)
            leftProd *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            right[i] = rightProd
            rightProd *= nums[i]
        
        output = []
        for i in range(len(nums)):
            output.append(left[i]*right[i])
        return output      