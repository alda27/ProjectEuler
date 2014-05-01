'''
Find the number of combinations of coins equaling 200
'''

target = 200
cu = [1,2,5,10,20,50,100,200]
ways = [0] * (target + 1)
ways[0] = 1
for i in xrange(0,8):
	for j in xrange(cu[i],target+1):
		ways[j] += ways[j-cu[i]]
print ways[target]