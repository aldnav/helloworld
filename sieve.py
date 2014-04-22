# MACHINE EXERCISE DAY 2: SIEVE REVISION
# @author Aldrin A. Navarro

def get_primes(lim):
	p = 2
	prime_numbers = range(p, lim+1)
	
	for n in prime_numbers:
		if n != 'x':
			next = n + 1
			while (next <= lim):
				if next % n == 0 and prime_numbers[next-p] != 'x':
					prime_numbers[next - p] = 'x'
				next += 1
				
	while 'x' in prime_numbers:
		prime_numbers.remove('x')
		
	return prime_numbers


if __name__ == '__main__':
	n = 20
	print get_primes(n)
