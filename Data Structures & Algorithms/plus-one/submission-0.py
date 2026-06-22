class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        lastdigit = len(digits) - 1
        newnum = digits[lastdigit] + 1
        if newnum > 9:
            carry = True
            digits[lastdigit] = 0
        else:
            digits[lastdigit] = newnum
        for i in range(len(digits)-2, -1, -1):
            if carry == True:
                newnum = digits[i] + 1
                if newnum > 9:
                    digits[i] = 0
                else:
                    digits[i] = newnum
                    carry = False

        if carry == True:
            digits.insert(0, 1)
        return digits