#Find the 10001th prime number
import time

def findPrimeNumberIndex(n):
	primeNumbers = []
	x = 2
	i = 0
	while i < n:
   		if all(x % j != 0 for j in primeNumbers):
			i += 1
			primeNumbers.append(x)
		x += 1
	print primeNumbers[n-1]

def main():
	start = time.time()
	findPrimeNumberIndex(10001)
	print time.time() - start, "seconds"

if __name__ == "__main__":
    main()