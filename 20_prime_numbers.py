# prime number: only divisible by itself and 1, such as 2, 3, 5, 11, 13, 17, 19
# composite number: can be factored into smaller integers, such as 4 = 2x2, 6 = 2x3, 8 = 2x4...
# unit: 1, integer 1 is neither prime nor composite, it is called unit

# version 1: test all divisors from 2 through n-1 (skip 1 and n, because every number is divisible by itself and 1)

import math
import time
def is_prime_v1(n):
	"""Return True is n is a prime number. False otherwise."""
	if n == 1:
		return False # 1 is not prime
	for d in range(2, n):
		if n % d == 0:
			return False
		return True

# Test Function
for n in nrage(1, 21):
	print(n, is_prime_v1(n))
# this function takes a long time when used with a large data
# to improve our function, we will reduce the number of divisors we check

# version 2: test all divisors from 2 through sqrt(N)

def is_prime_v2(n):
        """Return True is n is a prime number. False otherwise."""
        if n == 1:
                return False # 1 is not prime
	max_divisor = math.floor(math.sqrt(n)) # to find the largest possible divisor
	for d in range(2, 1 + max_divisor): #we add 1 because we want to include the max_divisor to the range
		if n % d == 0:
			return False
		return True

# test function
for n in range(1, 21):
	print(n, is_prime_v2(n))

t0 = time.time()
for n in range(1, 100000):
	is_prime_v2(n)
t1 = time.time()
print("Time required: ", t1-t0)
# this technique is much better in terms of taking less time, but there is still some stuff we can do to make this function better

#version 3: 
#step 1: test if n is even
#step 2: test only odd divisors
#if the input is even and bigger than 2, we will find a divisor on the first step, but if the input is odd, it is a waste ro check the even divisors

def is_prime_v3(n):
        """Return True is n is a prime number. False otherwise."""
        if n == 1:
                return False # 1 is not prime

	# if it's even and not 2, then it's not prime
	if n == 2:
		return True
	if n > 2 and n % 2 == 0:
		return False

	max_divisor = math.floor(math.sqrt(n)) # to find the largest possible divisor
        for d in range(3, 1 + max_divisor, 2): #we add 1 because we want to include the max_divisor to the range, the range starts with 3 and we also added a third value, a step parameter.
                if n % d == 0:
                        return False
		return True

# test function
for n in range(1, 21):
	print(n, is_prime_v3(n))
t0 = time.time()
for n in range(1, 100000):
        is_prime_v3(n)
t1 = time.time()
print("Time required: ", t1-t0)

# almost twice as fast as version 2

