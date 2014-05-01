'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import time
abundantNumbers = []

def findAbundantNumbers(maxVal):
	for val in xrange(1,maxVal+1):
		if findSumOfProperDivisors(val) > val:
			abundantNumbers.append(val)

def findSumOfNumbersWhichCantBeSummedByTwoAbundantNumbers(maxVal):
	s = [False] * (maxVal+1)
	for i in abundantNumbers:
		for j in abundantNumbers:
			if i + j < maxVal+1:
				s[i + j] = True
			else:
				break
	tot = 0
	for count in xrange(1,maxVal+1):
		if s[count] == False:
			tot += count
	print tot

def findSumOfProperDivisors(n):
	#1 is always a factor
	sum = 1
	count = 2
	while True:
		if count * count > n:
			return sum
		if n % count == 0:
			if count > n / count:
				return sum
			elif count == n/count:
				return sum + count
			#sum the 2 factors
			sum += count + n / count
		count+= 1


def main():
	start = time.time()
	findAbundantNumbers(28123)
	findSumOfNumbersWhichCantBeSummedByTwoAbundantNumbers(28123)
	print time.time() - start, "seconds"

if __name__ == "__main__":
    main()