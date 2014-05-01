
def findPrimes(n):
	n+1
	x = list(xrange(n+1))
	x[1] = 0
	for i in xrange(2,n+1):
		if x[i] != 0:
			for j in xrange(i+i,n+1,i):
				if x[j] != 0:
					x[j] = 0
	primes = []
	for i in x:
		if i != 0:
			primes.append(i)
	return primes