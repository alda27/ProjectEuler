

def generate(n):
	return n * (3 * n - 1) / 2

def is_pent(n):
	x = ((24 * n + 1) ** 0.5 + 1) / 6
	if x % 1 == 0:
		return True
	return False

i = 1
d = 0
found = False

while found is False:
	n = generate(i)
	for j in xrange(i,1,-1):
		m = generate(j)
		if is_pent(n - m) and is_pent(n + m):
			found = True
			d = n - m
			break
	i+=1
	
print d



