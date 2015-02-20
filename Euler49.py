from SieveOfEratosthenes import findPrimes

primes = findPrimes(10000, 1000)
prime_set = set(primes)
digits_set = set()

def number_to_digits(a):
    """
    Convert number to list of digits
    """
    digits = []
    while a > 0:
        digits.append(a % 10)
        a = a / 10
    return digits

def digits_to_number(a, sort=False):
    """
    Convert list of digits to a number
    Option to sort the list before converting to number
    """
    total = 0
    count = 0
    if sort:
        a.sort()
    for x in a:
        total = total + x * 10 ** count
        count = count + 1
    return total

def hash_number(a):
    """
    Hash so can distinguish permutation of number has been tested
    """
    return digits_to_number(number_to_digits(a), True)

def find_prime_permutations(a):
    b = number_to_digits(a)
    permutations = []

    def permutate(s, p):
        if not s:
            permutations.append(p)
            return
        for i in xrange(0,len(s)):
            r = p[:]
            r.append(s[i])
            permutate(s[:i] + s[i + 1:], r)

    permutate(b, [])

    permutation_set = set()
    for x in permutations:
        number = digits_to_number(x)
        if number > 1000 and number in prime_set:
            permutation_set.add(number)
    return permutation_set

def primes_equal_dist_apart(s):
    a = list(s)
    for i in xrange(0, len(a)):
        for j in xrange(i + 1, len(a)):
            for k in xrange(j + 1, len(a)):
                if a[j] - a[i] == a[k] - a[j]:
                    print '{}{}{}'.format(a[i], a[j], a[k])

for prime in primes:
    if hash_number(prime) in digits_set:
        continue
    if prime < 1000:
        digits_set.add(hash_number(prime))
        continue
    permutations = find_prime_permutations(prime)
    primes_equal_dist_apart(permutations)
    digits_set.add(hash_number(prime))
