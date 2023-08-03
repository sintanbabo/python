print('-'*80)
print(f'FasterPrimeFinding')
print('-'*80)

def allPrimeUpTo(num):
    primes = [2]
    for number in range(3,num):
        sqrtNum = number ** 0.5
        for factor in primes:
            if number % factor == 0:
                break
            if factor > sqrtNum:
                primes.append(number)
                break
    return primes

print(allPrimeUpTo(100))
print('-'*80)
print(allPrimeUpTo(1000))
print('-'*80)