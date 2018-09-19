from mat import *
from vec import getitem as getvec


M4 = Mat(({'a','b','c'},{'a','b','c'}), {('a','a'):2,('a','b'):2,('a','c'):5, ('b','c'):3})
v4 = Vec({'a','b','c'},{'a':1,'b':1,'c':1})
M4*v4 == Vec({'a','b','c'},{'a':8, 'b':0,'c':3})
print(M4*v4, M4,v4)

def mat_vec(M,v):
    assert M.D[1] == v.D
    pre =({(i,j):getitem(M,(j,i))*vecget(v,V) for (i,V) in zip(M.D[1], v.D) for j in M.D[0]})
    print(pre)
    f = {k:0 for k in M.D[0]}
    for i in M.D[0]:
        for (k,v) in pre.items():
             print(i,'i',k,"k")
             if i in k[0]:
                 f[k[1]]= f[k[1]] + v
    return Vec(M.D[0], f)

print(mat_vec(M4,v4))








v3 = Vec({'a','b'},{'a':1,'b':1})
M3 = Mat(({'a', 'b'}, {0, 1}), {('a', 1): 1, ('b', 1): 1, ('a', 0): 1, ('b', 0): 1})
v3*M3 == Vec({0, 1},{0: 2, 1: 2})

v1 = Vec({1, 2, 3}, {1: 1, 2: 8})
M1 = Mat(({1, 2, 3}, {'a', 'b', 'c'}), {(1, 'b'): 2, (2, 'a'):-1, (3, 'a'): 1, (3, 'c'): 7})
#Vec({'a', 'b', 'c'},{'a': -8, 'b': 2, 'c': 0})

C = Mat(({0,1,2}, {'a','b'}), {(0,'a'):4, (0,'b'):-3, (1,'a'):1, (2,'a'):1, (2,'b'):-2})
D = Mat(({'a','b'}, {'x','y'}), {('a','x'):3, ('a','y'):-2, ('b','x'):4, ('b','y'):-1})
A = Mat(({0,1,2}, {0,1,2}), {(1,1):4, (0,0):0, (1,2):1, (1,0):5, (0,1):3, (0,2):2})
B = Mat(({0,1,2}, {0,1,2}), {(1,0):5, (2,1):3, (1,1):2, (2,0):0, (0,0):1, (0,1):4})
#    >>> A*B == Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31})
def mat_mat(A,B):

    B_vecs = [Vec(B.D[0], {i:getitem(B,(i,j)) for i in B.D[0] for j in B.D[1] if j == k}) for k in B.D[1]]
    print(B_vecs)
    print(A,'a', B,'b')
    R = A.D[0]
    C = B.D[1]
    new_mat = Mat((R,C),{(r,c):0 for r in R for c in C})
    print(new_mat, 'mewmat')
    C = list(B.D[1])
    columns = [matrix_vector_mul(A,v) for v in B_vecs]
    print(columns)
    column = ''
    for i in range(len(C)):
        column = columns[i]
        print(column, 'colunm', C[i], 'label')
        for (R,val) in column.f.items():
            setitem(new_mat,(R,C[i]),val)
    return new_mat


print(mat_mat(A,B))
print()
print(Mat(({0,1,2}, {0,1,2}), {(0,0):15, (0,1):12, (1,0):25, (1,1):31}))
