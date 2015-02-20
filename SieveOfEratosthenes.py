
def findPrimes(end=1000, ignore_under=0):
    end = end + 1
    x = list(xrange(end))
    x[1] = 0
    for i in xrange(2, end):
        if x[i] != 0:
            for j in xrange(i + i, end, i):
                if x[j] != 0:
                    x[j] = 0
    primes = []
    for i in x:
        if i != 0 and i >= ignore_under:
            primes.append(i)
    return primes
