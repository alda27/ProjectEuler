'''
Starting in the top left corner of a 2x2 grid, and only being able
 to move to the right and down, there are exactly 6 routes
  to the bottom right corner.

How many such routes are there through a 20x20 grid?

m+n   = m+n
n       m
'''
import math

def latticePath(n):
	print math.factorial(2*n)/(math.factorial(2*n-n)*math.factorial(n))

def main():
	latticePath(20)

if __name__ == "__main__":
    main()