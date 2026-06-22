class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = (re.sub(r'[^a-zA-Z0-9]', '', s)).lower()
        i = 0
        j = len(newstring) - 1

        while i <= j:
            if newstring[i] != newstring[j]:
                return False
            i += 1
            j -= 1
        return True

        