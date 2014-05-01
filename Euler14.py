'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Which starting number, under one million, produces the longest chain?
'''

mLength = 100000000
m = [0] * mLength

def findLongestChain(l):

	longestChain = 0
	number = 0
	for i in xrange(2,l+1):
		calculateLengths(i)

	for i in xrange(2,l+1):
		if m[i] > longestChain:
			number = i
			longestChain = m[i]
	print "Longest chain: ",longestChain
	print "Number: ", number

def calculateLengths(n):
	if m[n] != 0:
		return
	x = []
	count = 1
	while n > 1:
		x.append(n)	
		n = collatzTransform(n)
		if n < mLength+1:
			if m[n] != 0:
				for i in x:
					if i < mLength+1:
						m[i] = m[n] + count
					count -= 1
				return
		count += 1		

	for i in x:
		m[i] = count
		count -= 1

def collatzTransform(b):
	if b % 2 == 0:
		return b / 2
	else:
		return (3 * b) + 1

def main():
	findLongestChain(1000000)

if __name__ == "__main__":
    main()