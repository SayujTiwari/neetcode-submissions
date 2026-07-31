class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        Rm = len(matrix) - 1
        Lm = 0
        rowLen = len(matrix[0])-1
        tarMat = 0

        while Lm <= Rm:
            middleM = (Rm+Lm)//2
            if target > matrix[middleM][rowLen]:
                Lm = middleM + 1
            elif target < matrix[middleM][0]:
                Rm = middleM - 1
            else:
                tarMat = middleM
                break

        l = 0
        r = rowLen
        while l <= r:
            middle = l + (r - l) // 2

            if matrix[tarMat][middle] == target:
                return True
            elif matrix[tarMat][middle] > target:
                r = middle - 1
            else:
                l = middle + 1

        return False