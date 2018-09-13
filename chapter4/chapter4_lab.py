from matutil import listlist2mat
from vec import *
from mat import *
from GF2 import *

#task 4.14.1 
[[one,0, one, one], [one, one, 0, one], [0,0,0,one], [one, one, one, 0], [0, 0, one, 0], [0, 0, one, 0], [0, one, 0, 0], [one, 0, 0, 0]] 
G = listlist2mat([[one,0, one, one], [one, one, 0, one], [0,0,0,one], [one, one, one, 0], [0, 0, one, 0], [0, 0, one, 0], [0, one, 0, 0], [one, 0, 0, 0]] 
)
print(G.f)
print(G.D)
#task 4.14.2 encode [one, 0, 0, one]
p = Vec({0,1,2,3},{0:one,1: 0,2: 0,3: one})
print(p) 
print(matrix_vector_mul(G,p))
c = G*p
print(c)

M = listlist2mat([[0,1], [2,3]])
V = Vec({0,1}, {0:5,1:6})
print(M*V) 

N1 = Mat(({1, 3, 5, 7}, {'a', 'b'}), {(1, 'a'): -1, (1, 'b'): 2, (3, 'a'): 1, (3, 'b'):4, (7, 'a'): 3, (5, 'b'):-1})
u1 = Vec({'a', 'b'}, {'a': 1, 'b': 2})
print(N1.D, u1.D)
print(N1*u1)

N1*u1 == Vec({1, 3, 5, 7},{1: 3, 3: 9, 5: -2, 7: 3})
