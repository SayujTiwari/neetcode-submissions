class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # start both pointers on left 
        # if len of window > len(s1)
        # if this 
        countS1 = {}
        countS2 = {}
        l =0 
        
        if len(s1) > len(s2):
            return False

        for c in s1:
            countS1[c] = 1 + countS1.get(c, 0) 
        
        for r in range(len(s2)):
            if (r-l+1) <= len(s1):
                countS2[s2[r]] = 1 + countS2.get(s2[r], 0) 
                # check with countS1
            else:
                countS2[s2[l]] = countS2.get(s2[l]) - 1 
                if countS2[s2[l]] == 0:
                    del countS2[s2[l]]
                l+=1
                countS2[s2[r]] = 1 + countS2.get(s2[r], 0) 
            if (r-l+1) == len(s1):
                if countS1 == countS2:
                    return True
        return False