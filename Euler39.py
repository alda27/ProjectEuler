'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
import math

n = [0]*1001;

for a in xrange(1,1000):
	for b in xrange(a,1000):
		p = (a ** 2 + b ** 2) ** 0.5 + a + b;
		if p > 1000:
			break;
		if p.is_integer():
			print p;
			n[int(p)] += 1;

index = 0;
for i in xrange(1,1001):
	if n[i] > n[index]:
		index = i;

print index