class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # skipping non alpha numeric chars on the left
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # skipping non alpha numeric chars on the right
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1 
        return True 
        
    def alphaNum(self, c):
        # Checks if character is alphaNumeric (A-Z, a-z, 0-9)
        # input: character c
        # output: boolean
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord (c) <= ord('z') or
         ord('0') <= ord(c) <= ord('9'))