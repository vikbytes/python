# https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80

import math

def leibniz(t):
    s = 0
    for r in range(t):
        s = s + ((-1)**r)/(2 * r + 1)
    return 4*s        

print("Estimated value:", leibniz(int(input("Desired number of iterations: "))))
print("True value: ", math.pi)