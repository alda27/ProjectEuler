#Find the largest palindrome made from the product of two 3-digit numbers.

def main():
	print max(x * y
   		for x in xrange(999,100,-1)
    		for y in xrange(999,100,-1)
    			if str(x*y) == str(x*y)[::-1])


if __name__ == "__main__":
    main()