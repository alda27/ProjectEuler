#What is the value of the first triangle number to have over five hundred divisors?

def findNumber():
	n = []
	n.append(0)
	i = 1
	while True:
		f = 2
		n.append(n[i-1]+i)
		#Induced that even numbers have more divisors than odd numbers
		if n[i] % 2 == 0:
			for j in xrange(2,i/2):
				if n[i] % j == 0:
					f += 2
				if f >= 500:
					return n[i]
		i+=1

def main():
	print findNumber()

if __name__ == "__main__":
    main()