#Find sum of all prime numbers under 2000000

def findSum(n):
	total = 0
	x = []
	for i in xrange(0,n+1):
		x.append(True)

	for i in xrange(3,n+1):
		if x[i-1] == True:
			total += i-1
			for j in xrange(i-1,n+1,i-1):
				if x[j] == True:
					x[j] = False
	print total



def main():
	findSum(2000000)

if __name__ == "__main__":
    main()