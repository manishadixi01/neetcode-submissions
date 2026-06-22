class Solution:
    def isHappy(self, n: int) -> bool:
        remember = []
        number = n
        remember.append(number)
        while number != 1:
            sum = 0
            while number > 0:
                sum += (number%10) ** 2
                number //= 10
            if sum not in remember:
                remember.append(sum)
                number = sum
            else:
                return False
        return True
        