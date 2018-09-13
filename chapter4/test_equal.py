from mat import *
from vec import getitem as getvec

v3 = Vec({'a','b'},{'a':1,'b':1})
M3 = Mat(({'a', 'b'}, {0, 1}), {('a', 1): 1, ('b', 1): 1, ('a', 0): 1, ('b', 0): 1})
v3*M3 == Vec({0, 1},{0: 2, 1: 2})

v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
#Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0})

def mat_test(M,v):
    assert M.D[0] == v.D
    print(v.D, "v.D")
    vec_values = {k:getvec(v,k) for k in v.D}
    mat_values = {(i,j):getitem(M,(i,j)) for i in M.D[0] for j in M.D[1]}

    print(vec_values, 'vec')
    print(mat_values,'mat')
    f = {k:0 for k in M.D[1]}
    print(f)
    for i in M.D[1]:
        for (k,v) in :
             if i in k:
                 f[k[1]]+=v
    return Vec(M.D[1], f)

print(mat_test(M1,v1))
