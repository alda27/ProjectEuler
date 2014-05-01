'''
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Observations:
Can't be even because they will always have a terminating zero.
Can be any odd number, prime or not, because 9 is observed to have recurring digits
'''
import time
import re

def findHighestNumber():
	highestNum = 0
	sequenceLength = 0
	for i in xrange(1000,0,-1):
		if sequenceLength > i:
			break;
		foundRemainders = [0]*i
		value = 1
		length = 0
		while foundRemainders[value] == 0 and value != 0:
			foundRemainders[value] = length
			value *= 10
			value %= i
			length += 1
		if length - foundRemainders[value] > sequenceLength:
			sequenceLength = length - foundRemainders[value]
			highestNum = i
	print highestNum

def main():
	start = time.time()
	findHighestNumber()
	print time.time() - start, "seconds"

if __name__ == "__main__":
    main()