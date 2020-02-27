'''
Truncatable primes - Problem 37 Project Euler.
==================
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
-------------------------------------------------------------
El numero 3797 tiene una propiedad interesante. Siendo primo este mismo, y es posible eliminar digitos continuamente desde la derecha hacia la izquierda, y permanecer primo en cada etapa:

Izquiera-Derecha                Derecha-Izquierda
3797                            3797
797                             379
97                              37
7                               3

Encuentra la suma de solo los 11 primeros primos que son ambos 'truncatable' de la izquierda a la derecha y derecha a la izquierda.

NOTE: 2, 3, 5, 7 no son considerados para ser primos 'truncatable'.
'''
import time
start = time.time()
##########################################
# Sieve of Erotosthenes
# One of the best algorithm to generate prime numbers

# generating n first primes with sieve of Erotosthenes.
def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = False

    for i in range(3, int(n), 2):
        index = i * 2
        while index < n:
            is_prime[index] = False
            index = index + i

    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime
# calling the function sieve()
primes = sieve(1000000)

# verifying if a number is prime
def isPrime(n):
    if n in primes:
        return True
    return False

# function that verify if a number is truncatable from Left-Right and Right-Left
def isTruncatable(p):
    numberL = p; numberR = p
    while len(str(numberR)) > 1:
        numberR = numberR//10
        exp = len(str(numberL)) - 1
        numberL = numberL % (10 ** exp)
        if not (isPrime(numberL)) or not (isPrime(numberR)):
            return False
    return True

# giving a number, verify if the number is truncatable and its descomposition from L-R and R-L...
def truncatablePrime(number):
    sum = 0; count = 0
    for i in primes[5:]:
        if count == 11: break
        if isTruncatable(i):
            print(i)
            sum += i
            count += 1
    return sum

# The correct answer is = 748317

# Test
number = 3797
print("SUM: ", truncatablePrime(number))

##########################################
# time at the end of the program execution
end = time.time()
# printing the execution time
print(end - start)
