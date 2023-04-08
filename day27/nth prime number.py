def is_prime(k):
    if k == 3 or k == 5:
        return True

    if k % 3 == 0 or k %5== 0:
        return False

    for i in range(3, k//2, 2):
        if k % i == 0:
            return False
    return True


def findNthPrime(n):
    # Write your code here.
    if n == 1:
        return 2
    i = 3
    ct = 1
    while True:
        if is_prime(i):
            ct += 1
            if ct == n:
                return i
                
        i += 2
        
        

""" Other Ways"""     

def isPrime(k):
 
    # Corner cases
    if (k <= 1):
        return 0
    if (k == 2 or k == 3):
        return 1
 
    # below 5 there is only two prime numbers 2 and 3
    if (k % 2 == 0 or k % 3 == 0):
        return 0
 
  # Using concept of prime number can be represented in form of (6*k + 1) or(6*k - 1)
    for i in range(5, 1 + int(k ** 0.5), 6):
        if (k % i == 0 or k % (i + 2) == 0):
            return 0
 
    return 1
 
# function which gives prime at position n
def findNthPrime2(n):
    i = 2
    while(n > 0):
 
        # each time if a prime number found decrease n
        if(isPrime(i)):
            n -= 1
 
        i += 1  # increase the integer to go ahead
 
    i -= 1  # since decrement of k is being done before
    # Increment of i , so i should be decreased by 1
    return i






primes = []
 
# Function to generate N prime numbers using 
# Sieve of Eratosthenes
def SieveOfEratosthenes():
     
    n = 1000005
     
    # Create a boolean array "prime[0..n]" and
    # initialize all entries it as true. A value
    # in prime[i] will finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
     
    p = 2
    while (p * p <= n):
           
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == True):
               
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
                 
        p += 1
       
    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            primes.append(p)
   
def findNthPrime3(n):
    SieveOfEratosthenes()
    return primes[n-1]







        
print(findNthPrime(115))
print(findNthPrime2(115))
print(findNthPrime3(115))







