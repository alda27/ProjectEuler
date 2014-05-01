#Find the smallest number divisible by each number 1 - 20
from Power import Power

#prime factorization
def primeFactorization(maxNum):
    primeNumbers = [2,3,5,7,11,13,17,19]
    powerArray = []
    
    #Find all the prime number factors and their exponents
    # take top half of range, because bottom half are CM of top half
    for i in range(maxNum/2+1,maxNum+1):
        index = 0
        power = None
        while i > 1:
            primeN = primeNumbers[index]
            if power is None:
                power = Power(primeN,0)
            if i % primeN == 0:
                i /= primeN
                power.addexponent()
            else:
                powerArray.append(power)
                power = None
                index += 1
        if power is not None:
            powerArray.append(power)

    product = 1
    for p in primeNumbers:
        if p <= maxNum:
            product *= max(x.getTotal()
                for x in powerArray
                    if x.getBase() == p)
    print product


def main():
    primeFactorization(20)

if __name__ == "__main__":
    main()

#brute force
#def smallestMultiple(maxNum):
#    i = maxNum
#    while(any(i % x != 0 for x in xrange(maxNum/2+1,maxNum))):
#        i += maxNum
#    return i