"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def power(base, exp):
    """
    Trick is to modulus by 10 ** 10 to only keep the last 10 digits to prevent from surpassing max_int value
    """
    total = base
    for _ in xrange(0, exp - 1):
        total = total * base % (10 ** 10)
    return total

def _sum(a, b):
    return (a + b) % (10 ** 10)

count = 1000
x = 0
for i in xrange(1, count + 1):
    y = power(i, i)
    x = _sum(x, y)

print x
