class Solution:
    def validPalindrome(self, s: str) -> bool:
        first = 0
        last = len(s) - 1
        while first < last:
            if s[first] != s[last]:
                return self.isPalindrome(s, first + 1, last) or self.isPalindrome(s, first, last - 1)
            first += 1
            last -= 1
        return True
    
    def isPalindrome(self, s, first, last):
        while first < last:
            if s[first] != s[last]:
                return False
            first += 1
            last -= 1
        return True


        