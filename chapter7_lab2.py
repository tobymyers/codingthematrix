#lab implementing the quadratic sieve to factor large square roots
from independence import *
from matutil import *
from echelon import *
from GF2 import one
from random import randint
import math
from factoring_support import intsqrt, dumb_factor, primes, prod
from vec import Vec

#7.8.1

def root_recur(N,a):
    pos_b = math.sqrt((a**2)-N)
    print(pos_b, 'pos_b')
    if pos_b % int(pos_b) == 0:
        b = pos_b
        return a - b, a + b
    else:
        return root_recur(N,a+1)

def root_method(N):
    a = intsqrt(N)+1
    return root_recur(N,a)

#print(root_method(118))
#tested with 55, 77, 14667, and 118.  runs out of recursions for all but 55 and 77
#sometimes fails because it iterates through the range that would have worked w/out finding anything, then it goes forever.
#could add a condition that says if pos_b == N, return None

#7.8.2
def gcd(x,y): return x if y == 0 else gcd(y,x%y)
n = [randint(180475307589798,4842978740927047937)for i in range(3)]
r,s,t = n[0],n[1],n[2]
a,b = r*s, s*t
print(a,b)
d = gcd(a,b)
assert a%d == 0
#assert (a/d) * d == a this doesn't work b/c python gets a little wacky here, but the theory is good
assert b%d == 0
assert d >= s
print(d, a/d, a/d * d) #holy shit Euclid was a smart cookie

#7.8.3
N = 367160330145890434494322103
a = 67469780066325164
b = 9429601150488992
c = (a*a - b*b )/N
print(c)
print(gcd(N, a-b))
#gdc of N and a-b is 19117318483477

#7.8.4
primeset = {2,3,5,7,11,13}
Ns = [12, 154, 2*3*3*3*11*11*11*13, 2*17,2*3*5*7*19]
[print(dumb_factor(x, primeset)) for x in Ns]
#correct answer for first 3, returned none for last two b/c 17 and 19 not in primeset


#7.8.5
def int2GF2(i):
    if i % 2 == 0:
        return 0
    else:
        return one

#7.8.6
def make_Vec(primeset, factors):
    return Vec(primeset,{factor[0]:int2GF2(factor[1]) for factor in factors})

print(make_Vec({2,3,5,7,11},[(3,1)]))

#7.8.7
#the interesting part ...
def find_candidates(N, primeset):
    roots = []
    rowlist = []
    x = intsqrt(N)+2
    while len(roots) < len(primeset) + 1:
        factors = dumb_factor(x*x-N, primeset)
        if factors == []:
            pass
        else:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))
        x += 1
    return roots, rowlist

roots, rowlist = find_candidates(2419,primes(32))

#7.8.8
a = 53 * 77
b = 2 * (3 **2 ) * 5 * 13
divisor = gcd(a -b, 2419)
print(divisor) #41
assert 2419%divisor == 0

c = 52 * 67 * 71
print(c)
d = 2 * (3**2) * 5 * 19 * 23
print(d,'cd')
divisor2 = gcd(2419,c-d)
print(divisor2) #returned 2419, which is valid I think, b/c that just means that c-d
#is a multiple of 2149 c-d == 86 * 2419
print((c-d )/ 2419)

#7.8.9
M = transformation_rows(rowlist)
Mmat = rowdict2mat(M)
A =rowdict2mat(rowlist)
print(A, 'rowlist')
print(Mmat, 'm')
print(Mmat*A)
row = -1

def find_a_and_b(M,roots,N, row):
    v = M[row]
    alist = [roots[k] for (k,v) in v.f.items() if v == one]
    a = prod(alist)
    c = prod({a*a - N for a in alist})
    b = intsqrt(c)
    if b * b == c:
        return a,b
    else:
        row -= 1
        return find_a_and_b(M,roots,N,row)

#a,b = find_a_and_b(M[10], roots, 2419)
#print(gcd(a-b, 2419))
#print(((a-b) * (a+b))/2419)

#7.8.11
N = 2461799993978700679
primelist = primes(1000)
def find_divisor(N,primelist):
    roots, rowlist = find_candidates(N, primelist)
    M = transformation_rows(rowlist)
    print('made_m,')
    row = -1
    while True:
        a,b = find_a_and_b(M,roots,N,row)
        divisor_test = gcd(a-b, N)
        if divisor_test % int(divisor_test) == 0 and divisor_test/N != 1:
            return a,b, divisor_test
        else:
            print('trying a new row')
            row -= 1


a,b,divisor = find_divisor(N,primelist)
print(divisor,"divisor of N")
print(N/divisor ,"N/divisor")


#7.8.12/13
N = 20672783502493917028427
primelist = primes(1000)
a,b,divisor = find_divisor(N,primelist)
print(divisor,"divisor of N")
print(N/divisor ,"N/divisor")
#factor is 16794489742507
