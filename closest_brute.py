# Brute force solution

def distance(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**(1/2)

def closest(x):
    n = len(x)
    mind = 999999999999
    a = -1
    b = -1
    for i in range(n-1):
        for j in range(i+1,n):
            d = distance(x[i], x[j])
            if d < mind:
                mind = d
                a = i
                b = j
    # print('Points:', x[a], x[b])
    # print('Distance:', mind)
