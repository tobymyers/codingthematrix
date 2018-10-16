#7.5 show row space and column space to be equivalent
from GF2 import *
from matutil import *
from solver import solve
from The_Basis_problems import *
from independence import *
from vecutil import *
"""A [120]
     [021]
row space == [1,0][0,1]
column space == [1,0][0,1]
row space == column space therefore they have the same span
and both span R2

B
[1400]
[0220]
[0011]
row space == [140][020][001]
column space == [100][420][001]
rank rs == rank cs because both are bases therefore linearly indpendent
therefore not superfluous.  definition of row rank is rank of basis of rows

C
[1]
[2]
[3]
row basis == [1]
column basis == [1]
this is a point, I think"""

#6.7.6
def my_is_independent(L):
    """procedure that uses rank to test whether or not a set is indpendent using the concept of rank.  The idea here is that
    a basis for any Span must have rank == that span. E.g. a basis for r3 is 001 010 100. All bases are the same size, so any basis for R3 will have rank 3.  Thus, if the length of a se of vectors is > it's rank,
    there must be a linear dependency."""
    return rank(L) == len(L)

L = [list2vec(l) for l in [[2,4,0],[4,5,6],[0,0,7]]]
print(my_is_independent(L))
#6.7.7

def my_rank(L):
    """uses subset basis to find a basis for L, then finds the length of that basis.  Because all bases are the same size,
    we can know dimension L and therefore rank L"""
    return len(subset_basis(L))

L = [list2vec(l) for l in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]]
print(my_rank(L))

#6.7.8 prove that if a vector space has dimension N then N+1 of it's vectors are linearly dependent.
"""let V be a vector space of dimension N and S be a basis for V.  By the morphing lemma, a set of linearly independent vectors contained in the generators for V will have at most
|generators|.  By theorem 6.1.3, the smallest set of generators must be a basis.  By proposition 6.2.4, rank S (the dimension of the vector space V) <= |S|.  So, dim V == dim S == N
All bases have the same size (rank N), and by definition span the entire vector space V.  Therefore, any additional vector added to S already exists in the span, and by the definition of
linear dependence is linearly dependent.  Any such vector added to S would bring make rank S == N+1.  All of S in contained in V, therefore this holds for V as well as S"""

#6.7.9
def is_solution(A, x, b):
    residual = b - A * x
    if residual * residual <= 10**-14:
        return True
    else:
        return False

def direct_sum_decompose(U_basis, V_basis, w):
    """finds the u in U and v in V that were added to create the vector w in the direct sum
    uses the fact that U_basis  union V_basis is a basis for V direct sum U  """

    U_V_basis = U_basis + V_basis
    A = coldict2mat(U_V_basis)
    u_plus_v = solve(A,w)
    print(u_plus_v)
    print(list(u_plus_v.D))
    if not is_solution(A,u_plus_v, w):
        return "not a solution"
    else:
        print(A*u_plus_v)
        list_D = list(u_plus_v.D)
        u_D = set(list_D[:len(U_basis)])
        v_D = set(list_D[:len(V_basis)])
        print(u_D, v_D)
        u_coeffs = Vec((u_D),{k:u_plus_v.f[k] for k in u_D})
        v_coeffs = Vec(v_D,{k:u_plus_v.f[k+len(u_D)] for k in v_D})
        print(u_coeffs, v_coeffs)
        u = coldict2mat(U_basis) * u_coeffs
        v = coldict2mat(V_basis) * v_coeffs
        return [u, v] #running into some very weird rounding errors here, but theory is correct.

U_basis = [list2vec(l) for l in [[2,1,0,0,6,0],[11,5,0,0,1,0],[3,1.5, 0,0,7.5,0]]]
V_basis = [list2vec(l) for l in [[0,0,7,0,0,1],[0,0,15,0,0,2]]]

print(direct_sum_decompose(U_basis, V_basis, list2vec([2,5,0,0,1,0])))

#6.7.10
def is_invertible(M):
    """tests to see if a matrix is invertible based on the criteria that it's square
    and that the columns are linearly independent.  Implied is that the rows are also linearly
    independent"""
    cols = mat2coldict(M)
    rows = mat2rowdict(M)
    col_vals = [vec for vec in cols.values()]
    return len(cols) == len(rows) and my_is_independent(col_vals)

m1 = listlist2mat([[1,2,3],[3,1,1]])
m2 = listlist2mat([[1,0,1,0],[0,2,1,0],[0,0,3,1],[0,0,0,4]])
print(is_invertible(m2))

#6.7.13
def find_inverse(GF2_M):
    """finds the inverse of a matrix over GF2, using the fact that a matrix * it's inverse is the identity matrix"""
    assert is_invertible(GF2_M) == True
    cols = mat2coldict(GF2_M)
    b_list = [Vec({i for i in range(len(cols))},{i:one}) for i in range(len(cols))]
    print(b_list)
    inverse_vecs = [solve(GF2_M, b) for (col, b) in zip( cols,b_list)]
    inverse = coldict2mat(inverse_vecs)
    identity = GF2_M * inverse
    return inverse, identity

mat = listlist2mat([[0,one,0],[one, 0,0],[0,0,one]])
print(find_inverse(mat))
