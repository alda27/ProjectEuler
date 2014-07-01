'''
Find sum of pandigital product/multiplier/multiplicand from 1 - 9
'''
import math

nMin = 1000
nMax = 10000

def isNineDigits(product,a,b):
	if len(str(product))+len(str(a))+len(str(b)) == 9:
		return True
	return False
def isPandigital(product,a,b):
	testStr = str(product) + str(a) + str(b)
	digitArray = [False]*9
	for digit in testStr:
		index = ord(digit)-ord('0')-1
		if index == -1:
			return False
		elif digitArray[index] == False:
			digitArray[index] = True
		else:
			return False
	return True


#find factors of all products and check if 9 digits and pandigital
total = []
for product in xrange(nMin,nMax+1):
	for factor in xrange(2,int(math.ceil(product**1/2))):
		if product % factor == 0:
			factor1 = product / factor
			if isNineDigits(product,factor,factor1):
				if isPandigital(product,factor,factor1):
					if product not in total:
						total.append(product)
print sum(total)