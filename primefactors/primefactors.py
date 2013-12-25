def is_prime(num):
  if num < 2: raise Exception("Tough Question")
  return not any((num % i == 0 for i in xrange(2, int(num**0.5)+1)))

def prime_factors(num):
  if is_prime(num):
    return [num]
  else:
    for i in xrange(2, int(num**0.5)+1):
      if num % i == 0:
        return primeFactors(num/i) + primeFactors(num/(num/i))
