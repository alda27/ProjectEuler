'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

Calculate the product of each digit with 10^1, 10^2 ... 10^6
'''
def f(digit):
	exponent = 1;
	number = 1;

	while True:
		numberRange = 10 ** exponent - 10 ** (exponent - 1);
		digitRange = numberRange * exponent;

		if digit > digitRange:
			digit -= digitRange;
			number += numberRange;
			exponent += 1;

		else:
			digit -= 1;
			mod = digit % exponent;
			divisor = digit / exponent;
			strNumber = str(number + divisor);
			return int(strNumber[mod:mod+1]);

print f(1) * f(10) * f(100) * f(1000) * f(10000) * f(100000) * f(1000000) 


