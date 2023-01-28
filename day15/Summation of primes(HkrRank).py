#!/bin/python3

# https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem

'''Most optimized codes for
        1 -> Checking a number is prime
        2 -> Generating primes in a range
        3 -> sum of all primes till N  N <= 1000001
                            
'''

'''
Sample Input:
2
5
10

Sample Output:
10
17
'''


"""Attempt 1: TLE  (6/8)"""
def sieve_of_eratosthenes_primes(N):
    sm = 0
    is_prime = [1 for num in range(N)]
    is_prime[0] = 0 # this is because indexing starts at zero
    is_prime[1] = 0 # one is not a prime, but don't mark all of its multiples!

    def set_prime(num):
        "num is a prime; set all of its multiples in is_prime to zero"
        for x in range(num*2, N, num):
            is_prime[x] = 0

    # iterate over all integers up to N and update the is_prime array accordingly
    for num in range(N):
        if is_prime[num] == 1:
            set_prime(num) 
            sm += num
    return sm
    

    
"""Attempt 2: TLE  4/8)"""
def generate_primes_in_range(end):
    start = 0 
    numbersList = list(range(start, end+1)) 
    for i in range(2,int(end**0.5)+1): 
        for j in range (i*i, end+1, i): 
            print(numbersList)
            if j in numbersList: 
                numbersList.remove(j) 
    # print(numbersList)
    return sum(numbersList) - 1
    
    
    
"""Attempt 3: Wrong answer and TLE  (3/8)"""
def is_prime(number):
    if number <= 1:
        return False
    if number == 2 or number == 3 or number == 5 or number == 7:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while(i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return False
        i = i + 6
        return True
    
def solve3(end):
    sm = 0
    for num in range(end):
        print(num, is_prime(num))
        if is_prime(num):
            sm += num
        
    return sm

    
    
"""Attempt 4: TLE  5/8)"""
def solve2(n):
    s = set()
    for i in range(2, n+1):
        for j in range(2, i+1):
            if(i % j == 0):
                s.add(j)
                break
    return sum(s)

    
   
"""Attempt 5: Success (8/8)"""
N = 10**6
sieve = [0]*N
def eratosthenes_sieve():
    # turn primes ..
    for i in range(3, N, 2):
        if sieve[i] == 0:
            sieve[i] = i
            for j in range(i*i, N, i): sieve[j] = 1    
    # .. into sums
    s = 2
    for i in range(3, N-1, 2):
        s += 0 if sieve[i] == 1 else sieve[i]
        sieve[i] = sieve[i+1] = s
    
eratosthenes_sieve()   # Call it only once.

def solve(n):
    return sieve[n]  

    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(solve(n))
