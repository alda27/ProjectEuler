'''
Find the product of the coefficients, a and b, for the quadratic expression 
that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''
from SieveOfEratosthenes import findPrimes

def f(a,b,n):
	return n ** 2 + a * n + b

def isPrime(x):
	if x in primes:
		return True
	return False

maxCoefficient = 1000
primes = findPrimes(10000)
consecutivePrimes = 0
a = 0
b = 0
for j in primes:
	if j > 1000:
		break
	for i in xrange(-maxCoefficient + 1,1,2):
		n = 0
		while isPrime(f(i,j,n)):
			n+=1
		if n > consecutivePrimes:
			b = i
			a = j
			consecutivePrimes = n

print a * b