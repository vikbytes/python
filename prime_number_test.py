# A simple (but inefficient) program for checking if a given number n is prime

def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        for i in (3, (n ** (1 / 2)), 2):
            if n % i == 0:
                return False
        else:
            return True

print(is_prime(int(input("Number: "))))