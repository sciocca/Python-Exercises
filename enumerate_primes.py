def primes(a):
    primes = []
    is_prime = [False,False] + [True] * (a-1)
    for p in range(2,a+1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p,a+1,p):
                is_prime[i] = False
    return primes



print(primes(1000))
#[2,3,5,7,11,13,17]