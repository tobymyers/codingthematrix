from mat import *
from vec import getitem as getvec

v3 = Vec({'a','b'},{'a':1,'b':1})
M3 = Mat(({'a', 'b'}, {0, 1}), {('a', 1): 1, ('b', 1): 1, ('a', 0): 1, ('b', 0): 1})
v3*M3 == Vec({0, 1},{0: 2, 1: 2})

v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
#Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0})

C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})

def mat_mat(A,B):
    B_vecs = [Vec(B.D[0], {i:getitem(B,(i,j)) for i in B.D[0] for j in B.D[1] if j == k}) for k in B.D[1]]
    print(B_vecs)
    new_vecs = [matrix_vector_mul(A,v) for v in B_vecs] #good till here
    #leaving this here for tonight
    A_B = Mat((A[0], B[1]), {(i,j):0 for j in A.D[0] for i in B.D[1]})
    print(A_B)
    pre =[{(i,j):getitem(A,(j,i))*vecget(v,V) for (i,V) in zip(A.D[1], v.D) for j in A.D[0]} for v in B_vecs]
    f = {(i,j):0 for i in A.D[0] for j in B.D[1]}
    for i in A.D[0]:
        for p in pre:
            print(p, "onevecf")
            for (k,v) in p.items():
                if i in k:
                     print(k,v, "kv")
                     f[k]+=v
    print(f)


    new_vecs = [matrix_vector_mul(A,v) for v in B_vecs] #good till here
    A_B = Mat((A[0], B[1]), {(j,i):v for (i,v) in v.f.items() for (a,j) in zip(new_vecs,B.D[1])})
    print(A_B)
mat_mat(C,D)
