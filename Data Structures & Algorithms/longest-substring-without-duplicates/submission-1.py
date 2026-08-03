class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        seen = set()
        best = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
                best = max(best, r-l)
            else:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l += 1
                l += 1 
                r += 1 

        return best















