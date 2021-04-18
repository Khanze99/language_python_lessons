

class Solution:
    def reverse(self, x: int) -> int:
        stack = ''
        minus = False

        if x >= 2**31-1 or x <= -2**31 or x == 0: return 0

        if x < 0:
            minus = True
            x = abs(x)

        while x != 0:
            pop = x % 10
            stack += str(pop)
            x //= 10

        rev = int(stack)
        if minus:
            rev = -rev

        if rev >= 2**31-1 or rev <= -2**31:
            return 0

        return rev