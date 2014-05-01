'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

import time
a = [0,1,2,3,4,5,6,7,8,9]

def findPermutation(permutation):
	perm = ""
	permutation -= 1
	maxVal = max(a)
	length = len(a)
	for i in xrange(0,length):
		f = factor(maxVal-i)
		j = permutation / f
		permutation = permutation % f
		perm += str(a[j])
		a.remove(a[j])
		if permutation == 0:
			break

	for i in xrange(0,len(a)):
		perm += str(a[i])
	print perm

def factor(n):
	if n < 2:
		return 1;
	product = 1
	for i in xrange(1,n+1):
		product *= i
	return product

def main():
	start = time.time()
	findPermutation(1000000)
	print time.time() - start, "seconds"

if __name__ == "__main__":
    main()