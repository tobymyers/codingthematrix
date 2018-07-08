from vec import *
from GF2 import *
from itertools import combinations
#3.2.15
"""1) x*([3,4]-2*[1,2])-y/2*([3,4]-3[1,2])==[x,y]
2) x(-[3,3]+2[2,2]-[1,1]+[0,1]) + y(2[2,2]-[3,3]-[1,1]-[0,1])== [x,y]
3) 0[1,1] +1[1,-1]+x[0,1]+y(1[1,1]+0[1,-1]-1[0,1]) == [x,y]"""

"""3.2.16
1) [0,0,1]==0[1,1,1]+0[0.4, 1.3, -2.2]+1[0,0,1]
2) [0,1,0]==-1/3.25(1[1,1,1]-2.5[0.4, 1.3, -2.2]-5.5[0,0,1])
3) [1,0,0]==1.25(1[1,1,1]-.76[0.4, 1.3, -2.2]-1.69[0,0,1])"""

#3.8.2
from random import randint
def get_random_vec(D): return Vec(D, {d:randint(0,5) for d in D})
def get_random_vec_list(D, n): return [get_random_vec(D) for i in range(n)]
D = {'a','b','c','d','e'}
L = get_random_vec_list(D,20)
def vec_select(L,k):
    out = []
    for vec in L:
        if getitem(vec, k) == 0:
            out.append(vec)
    return out

def vec_sum(D, L):
    out = {d:0 for d in D}
    for vec in L:
        for d,v in vec.f.items():
           out[d] += v
    return out

def vec_select_sum(D, L, k): return [vec_sum(D,vec_select(L,k))]
print(vec_select_sum(D, L, 'a'))
"""
#3.8.3
D = {'a','b', 'c'}
L = [Vec(D, {'a':one, 'b':one, 'c': one} ), Vec(D, {'a':one, 'b':0, 'c':0})]
def GF2_span(D, L):
    c_input = [0, one] * len(L)
    combo = set(combinations(c_input, len(L)))
    print(combo)
    #return {print(add(scalar_mul(L[0],c[0]), scalar_mul(L[1],c[1])))  for c in combo}
    #return {print(add(scalar_mul(vec, )(0],c[0]), scalar_mul(L[1],c[1])))  for C in combo for c, vec in zip(C, L)}
    # for C in combo:
    #     out = add(m)
    #     m = []
    #     for c, vec in zip(C, L):
    #         m.append(scalar_mul(vec,c))
    # print(out)
print(GF2_span(D, L))
#get a list of all possible combinations
#multiply each combo with vec
##need to make this solid no matter how long vec is

def standard(D, one):
    return [Vec(D, {k:one}) for k in D]

print(standard({1,2,3,4,5}, 1))
"""
