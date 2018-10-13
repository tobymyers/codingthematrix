#7.5 show row space and column space to be equivalent
from The_Basis_Problems.py import *
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
