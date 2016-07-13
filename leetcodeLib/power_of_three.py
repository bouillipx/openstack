__author__ = 'bouilli'
def isPowerOfThree(n):
    if n == 1:
        return True
    while n != 3:
        if n % 3 != 0:
            return False
        n /= 3
    return True
print isPowerOfThree(126)