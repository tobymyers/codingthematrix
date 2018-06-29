#2.14.1 add and subtract vectors u= [-1,3] and v = [0,4] and 3v - 2u. draw on same graph
# u + v == -1, 7 : u - v == -1, -1 3v - 2u == 0, 12 - 1, 6 == -1, 6

#2.14.2 v = [2, -1, 5] u = [-1,1,1]
# v+u == [1, 0, 5], v-u == [3, -2, 4], 2v - u == [5, -3, 9] v + 2u == [0, 1, 7]

#2.14.3 v = [0,one, one] u = [one, one, one]
#u+v == one, 0, 0 and u+v+u = 0, one, one #f(u) = u +v + u is the identity function of u, b/c in gf(2)
#repeating a vector cancels it out.

#2.14.4
from GF2 import *
from random import randint
from collections import Counter

a = [one, one, one ,0,0,0,0]
b = [0, one, one,one ,0,0,0]
c = [0,0,one, one, one,0,0,0]
d = [0,0,0, one, one, one,0]
e = [0,0,0,0, one, one, one]
f = [0, 0, 0,0,0,one, one]
u = [0,0, one,0,0,one, 0]

vecs = [a,b,c,d,e,f]
vecs_labels = ['a','b','c','d','e','f']

def solve_GF2_add(vecs, vecs_labels, u):
    """function to solve for subset of vecs that add up to u or
    report that none exists.  this is janky, but if i've done len(n)*10000 additions
    and haven't found the answer, it reports that none exists. True version is if it's not in the set of
    2^(n(n+1))/2 possibilities it doesn't exist. or just 2^n
    possibilities if you're counting blank as an answer """
    assert len(u) == len(vecs[0])
    trye = []
    subset = []
    ans = a
    count = 0
    while ans != u:
        rand = randint(0,5)
        trye =  vecs[rand]
        subset.append(vecs_labels[rand])
        ans = [t+a for (t,a) in zip(trye, ans)]
        count+=1
        if count == 100 * len(u):
            return('does not exist')
    histo = Counter(subset)
    dedupe = set()
    for label in vecs_labels:
        if histo[label]%2 != 0:
            dedupe.add(label)
    return dedupe,'==', ans

#for u1, e+d+c
#for u2, cancel e d+a+c

#2.14.15
print(solve_GF2_add(vecs, vecs_labels, [0,0,one,0,0,one, 0])) #adc
print(solve_GF2_add(vecs, vecs_labels,  [0,one,0,0,0,one, 0])) #does not exist
print(solve_GF2_add(vecs, vecs_labels,  [one,one ,one,0,0,one, 0])) #does not exist
print(solve_GF2_add(vecs, vecs_labels,  [one,one ,one,one,0,one, 0])) #efd

#2.14.6
