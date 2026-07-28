class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for i in s.lower():
            if i.isalnum():
                new_str += str(i)
            else:
                continue
        
        l = 0
        r = len(new_str)-1

        while l < r:
            if new_str[l] != new_str[r]:
                return False
            l += 1
            r -= 1
        return True        