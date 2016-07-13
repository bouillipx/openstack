__author__ = 'bouilli'

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    sum = 0
    tmp = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
    for i in xrange(len(s)):
        if i == len(s) - 1:
            sum += tmp[s[i]]
        elif tmp[s[i]] >= tmp[s[i+1]]:
            sum += tmp[s[i]]
        else:
            sum -= tmp[s[i]]

    return sum

print romanToInt('DCXXI')