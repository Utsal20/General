# Divide and conquer solution
import sys
from random import randint
from time import time
import closest_brute

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def closest(x):
    n = len(x)
    if n < 2:
        return sys.maxsize
    if (n == 2):
        return distance(x[0], x[1])
    
    x = sorted(x)
    x1 = closest(x[:int(n/2)])
    x2 = closest(x[(int(n/2)+1):])
    d = min(x1, x2)
    strip = []
    for i in range(n-1):
        if d > abs(x[i][0] - x[int(n/2)][0]):
            strip.append(x[i])
    
    strip = sorted(strip, key = lambda y: y[1])

    k = len(strip)
    for i in range(k-2):
        if (d > distance(strip[i], strip[i+1])):
            d = distance(strip[i], strip[i+1])
    
    return d

def gen_data(n):
    l = []
    for i in range(n):
        l.append((randint(0, sys.maxsize), randint(0, sys.maxsize)))
    return l

def run_tests():
    d = [100, 1000, 10000, 100000]
    for each in d:
        data = gen_data(each)
        t1 = time()
        closest(data)
        t2 = time()
        closest_brute.closest(data)
        t3 = time()
        print(each, t2-t1)
        print(each, t3-t2)

'''
test1 = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
print(closest(test1))
test2 = [(1,1), (1,1), (1,1), (1,1)]
print(closest(test2))
test3 = [(1,150), (1,100), (50,100), (50,150)]
print(closest(test3))

test3 = [(1,150), (1,100), (50,100), (50,150)]
print(closest_brute.closest(test3))
'''

run_tests()
