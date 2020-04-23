# https://en.wikipedia.org/wiki/Collatz_conjecture
n = int(input("\n n: "))
if(n <= 1):
    print("Please enter a number > 1.\n")
    exit(0)
steps = 0

while(True):
    if(n == 1):
        break
    if(n % 2 == 0):
        steps += 1
        n /= 2
    else:
        steps += 1
        n = 3*n + 1

print("Number of steps: ", steps)