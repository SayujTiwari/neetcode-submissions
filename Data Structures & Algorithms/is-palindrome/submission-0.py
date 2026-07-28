class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                newChar = char.lower()
                newStr += newChar


        reversedStr = ""
        for i in range(len(newStr) - 1, -1, -1):
            reversedStr += newStr[i]

        return reversedStr == newStr