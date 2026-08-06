class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r, M, sol = 0, 0, deque(), []
        for r in range(len(nums)):
            while M and M[-1] < nums[r]:
                M.pop()
            M.append(nums[r])
            if r > k - 1:
                if nums[l] == M[0]:
                    M.popleft()
                l += 1
            if r >= k - 1:
                sol.append(M[0])
        return sol

