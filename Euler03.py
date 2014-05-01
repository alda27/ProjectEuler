#What is the largest prime factor of the number 600851475143 ?

def largestPrimeFactor(num):
	divisor = 2
	while divisor <= num/2:
		if num % divisor == 0:
			num = num /divisor
			divisor = 2
		else:
			divisor += 1
	return num


def main():
    lpf = largestPrimeFactor(600851475143)
    print lpf


if __name__ == "__main__":
    main()