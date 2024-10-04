#!/usr/bin/python3
"Prime game function to determine winner between players"

def sieve_of_eratosthenes(n):
    """ Helper function to find all primes up to n using the Sieve of Eratosthenes """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes

def isWinner(x, nums):
    """ Determine the winner after x rounds of prime game """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    
    # Precompute number of primes up to each number
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)
    
    maria_wins = 0
    ben_wins = 0

    # Simulate each game
    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
