from independence import *
from vecutil import *
from matutil import *
from math import fabs
#necessary functions
def project_along(b,v):
    if v * v == 0:
        print(v,'v',b,'b')
    sigma = (b * v) / (v * v)
    return sigma * v

def project_orthogonal_1(b,v):
    return b - project_along(b,v)

def project_orthogonal(b,vlist):
    for v in vlist:
        b = b - project_along(b,v)
    return b

def aug_project_orthogonal(b,vlist):
    sigmadict = {len(vlist):1}
    for i,v in enumerate(vlist):
        if v*v == 0:
            print(v)
        sigma = (b * v) / (v * v)
        sigmadict[i] = sigma
        b = b - sigma * v
    return b, sigmadict

def orthagonalize(vlist):
    vstarlist = []
    for v in vlist:
        vstarlist.append(project_orthogonal(v, vstarlist))
    return vstarlist

def aug_orthagonalize(vlist):
    vstarlist = []
    sigmalist = []
    D = set(range(len(vlist)))
    for i,v in enumerate(vlist):
        (vstar, sigmadict) = aug_project_orthogonal(v, vstarlist)
        vstarlist.append(vstar)
        sigmalist.append(Vec(D,sigmadict))
    return vstarlist, sigmalist

def find_orthogonal_complement(U_basis, W_basis):
    Lstar = orthagonalize(U_basis + W_basis)
    return [vec for vec in Lstar[len(U_basis):] if vec*vec > 10**-20]

#9.1
#1
W_basis = [list2vec(l) for l in [[1,2,-3,1],[1,2,0,1],[3,1,0,1],[-1,-2,3,1]]]
U_basis = [list2vec(l) for l in [[0,0,3,2]]]
print(find_orthogonal_complement(U_basis, W_basis))
"""V_basis =
 0 1     2    3
---------------
 1 2 -1.38 2.08

    0    1     2      3
-----------------------
 0.37 0.74 0.411 -0.616

 0  1 2 3
---------
 2 -1 0 0"""

#2
W_basis = [list2vec(l) for l in [[1,0,0],[1,0,1]]]
U_basis = [list2vec([3,0,1])]
print(find_orthogonal_complement(U_basis, W_basis))
"""  0 1    2
-----------
 0.1 0 -0.3"""

#3
W_basis = [list2vec(l) for l in [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]]
U_basis = [list2vec(l) for l in [[-4,3,1,-2],[-2,2,3,-1]]]
print(find_orthogonal_complement(U_basis, W_basis))
"""     0     1       2      3
---------------------------
 0.419 0.391 -0.0782 -0.291

         0     1       2     3
------------------------------
 -1.11E-16 0.333 -0.0667 0.467"""

#9.11.2
#1 b/c W has no y component, and U has a y compononent, therefore U is not a
#subspace of W
#2 b/c U isn't a scalar of any b, one of which is  1.8, -3.14, 0.917

def lists2vec(list_of_lists):
    return [list2vec(l) for l in list_of_lists]

print(project_orthogonal(list2vec([2,-3,1]),lists2vec([[3,2,1],[5,2,-3]])))

#3
U_basis = lists2vec([[-4,-1,-3,-2],[0,4,0,-1]])
W_basis = lists2vec([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
V_basis = find_orthogonal_complement(U_basis,W_basis)
print(V_basis)
V = coldict2mat(V_basis)
U = rowdict2mat(U_basis)
print(U*V)
"""[Vec({0, 1, 2, 3},{0: 0.4624505928853755, 1: -0.07114624505928856, 2: -0.4031620553359684, 3: -0.2845849802371541}), Vec({0, 1, 2, 3},{0: 0.0, 1: 0.038461538461538505, 2: -0.11538461538461539, 3: 0.15384615384615388})]
"""

#4
#1 [2,-3]
#2 [3,-5]

#5
# U_list = [list2vec(l) for l in [[0,1,0],[0,0,1]]]
# W_list = [list2vec(l) for l in [[1,2,3],[2,1,0],[0,0,3]]]
# print(U_list, W_list)
# norm = find_orthogonal_complement(U_list, W_list)
# print(norm,'norm')
U_list = lists2vec([[2,1,-3],[-2,1,1]])
W_list = lists2vec([[1,0,1],[0,1,0],[1,1,0]])
normal = find_orthogonal_complement(U_list, W_list)
print(normal)

#pretty sure this is wrong
U_list = lists2vec([[3,1,4],[5,2,6], [2,3,5]])
a,b,c = U_list[0], U_list[1], U_list[2]
W_list = lists2vec([[1,0,1],[0,1,0],[1,1,0]])
normal = find_orthogonal_complement([a-c,b-c], W_list)
print(c,'c', c+normal[0])
print(normal)

#6
#1 [0,7] is the normal for the line [-7,0], which for [x,y] is [-y,x]
#2 [1,2] is a normal for the line [-2,1] which for [x,y] is [-y,x]


#7
#1[01,-1][-1,0,1]
#2 [100][001]

#8
#Theorem: for a Matrix a over the reals, the row rank equals the column rank
"""Let A be an RxC matrix.  Then the orthogonal complement of Row A is null A, the annihilator of Row A.
Lemma 9.6 states that if U is a subspace of W, and V is the orthoganol
     complement of U, then
     W == the direct sum of U and V.
     null A is the orthonogonal complement,
     so let Row A be U, and then V is Null A


The direct sum corollary states that the dimension of the direct sum will be
== to the sum of the dimensions of its two components.
     We therefore know that
     dim W is dim Row A + dim Null A
     I assert that dim W == |C| #number of columns of A
     #dont get how this next step works but I think it's correct
     Null A is the set of vecs that when multiplied by the rows == 0
     Row A is the space created by any linear combination of the rows.
     by the dot product def of Mv mult, A * null A must be part of W:

     therefore dim Row A + dim null A == number of columns of A

the kernel image theorem states that dim V == dim im V + dim ker V:
the kernel of a function is the null space of a matrix, so ker V == null A
the image of V in this context is colA, so dim im V == dim Col A.
thus dim V == dim colA + dim null A
V is the domain, i.e the set of columns to be multiplied by based on the linear combinations def of
matrix vector multiplication.

so, number of columns == dim Col A + dim null A and!
dim Col A + dim null A == dim Row A (not really proven) + dim null A
subtracting dim null A from both sides, we get dim Col A == dim Row A
or rank Col(A) == rank Row(A)

this is basically saying that if the matrix is a basis, its null space will be trivial.

#
