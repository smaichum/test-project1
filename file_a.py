import math
print('Hello World')

def gauss(x, mean, std):
    return math.exp(-0.5*x**2)

print(gauss(0.5, 1, 1))