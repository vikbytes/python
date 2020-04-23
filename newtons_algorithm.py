# https://en.wikipedia.org/wiki/Newton%27s_method
def newt(n, t):
    s = n*n
    g = s / 2
    for r in range(0,t):
        g = 0.5 * (g + ((n*n)/g))
        print(g)

n = int(input("The squarenumber: "))
t = int(input("Iterations: "))
newt(n, t)
