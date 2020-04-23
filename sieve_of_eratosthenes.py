# Implementation of the Sieve of Eratosthenes algorithm

# Limiting number (i.e. look only up to this number)
n = int(input("n: "))

numbers = list(range(2, n+1))
marked_numbers = []
p = 2

# Naive implementation of the algorithm
while(p <= n):
    t = 2 # Step for p
    m = t*p # The temporary value for the current number enumerated
    while(m <= n):
        if(m not in marked_numbers):
            marked_numbers.append(m)
        t += 1
        m = t*p
    p += 1
    while(True):
        if (p in marked_numbers):
            p += 1
        else:
            break

# Print out the sieved numbers, i.e. all primes below n
print("Primes below n:")
for x in numbers:
    if x in marked_numbers:
        continue
    else:
        print(x)