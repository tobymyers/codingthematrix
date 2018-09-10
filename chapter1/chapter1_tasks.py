# 1.4.1
# from plotting import plot
# S = {2 +2j, 3+2j, 1.75+ 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
# #plot(S, 4)
# #plot (a, 4) the plot module doesn't work.  Need to find a new one
#
# #1.4.17
# from math import e, pi
# n= 20
# print([e**((2*pi*1j)/v) for v in range(1,n)])
#
#1.5.1 decrypt flawed one time pad
from random import randint
import string

def possk():
    """creates set of tuples of all possible 5 bit key patterns. turns out there are 2**5 options"""
    s = set()
    for i in range(1000):
        t = []
        for i in range(5):
             t.append(randint(0,1))
        a = tuple(t)
        s.add(a)

    return s
def map():
    l = {z:list(format(i,'05b')) for (i, z) in zip(list(range(26)), list(string.ascii_lowercase))}
    return l
def map2():
    l = {format(i,'05b'):z for (i, z) in zip(list(range(26)), list(string.ascii_lowercase))}
    return l
def gf2add(a, b):
    if a + b == 2:
        return 0
    else:
        return a + b
def solve(map, possk, cypher):
    ans = ''
    for key in possk: #ll possible keys
        for c in cypher:
            chr = ''
            for k,a in zip(key, c):
                chr = chr + str(gf2add(k,a))
            if chr in map2:
                ans = ans + map2[chr]
            else:
                ans = ans + '?'
        ans = ans + '     '
    return ans

cypher = ((1,0,1,0,1),(0,0,1,0,0),(1,0,1,0,1),(0,1,0,1,1),(1,1,0,0,1),(0,0,0,1,1),(0,1,0,1,1),(1,0,1,0,1),(0,0,1,0,0),(1,1,0,0,1),(1,1,0,1,0))
possk = possk()
map2 = map2()
print(solve(map2, possk, cypher))
