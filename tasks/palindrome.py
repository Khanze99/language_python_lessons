
class Solution:
    def is_palindrome(self, x: int) -> bool:  # как до этого можно додуматься?
        if (x != 0 and x % 10 == 0) or (x < 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        return x == reverted_number or x == reverted_number // 10


class Palindrome:  # мое решение
    def isPalindrome(self, x: int) -> bool:
        palindrome_flag = False
        n = ''
        change_x = x
        if x >= 0:
            while True:
                n += str(change_x % 10)
                change_x //= 10
                if not change_x:
                    break
            try:
                if int(n) == x:
                    palindrome_flag = True
            except ValueError:
                ...

        return palindrome_flag
