from vecutil import *
from mat import Mat
from matutil import *
from GF2 import *
from solver import solve
#5.5.6 show that no independent set contains the zero vector
# let D = {(0,0), (7,7)}
#take any non-zero coefficient for the zero vector and zero for the non-zero vector, e.g.
#{4(0,0), 0(7,7)}
#in order for a set of vectors to be linearly dependent it must be possible to form the zero vector out of a linear combination
#of the vectors with at least one non-zero coefficient.  Any non-zero coefficient times the zero vector will evaluate to 0
#therefore there can be no linearly independent set that contains the zero vector.

#prove that the standard generators of FD form a basis. i.e. that all the generators for a field of domain D are the basis of that field
"""let the generators for FDn be represented by G = zero vectors of length D with zeros in the 'i'th location.
e.g empty =  [[0]*(len(D))] for i in range(len(D))]
 G = empty[i] = 1 for i in range(len(empty))

x,y,z...n can be formed by a combination of the generators e.g x[1,0,0....n] + y[0,1,0,0....n] ...n[0,0,0...1] so we know that G spans FD.  we also know that the vecs are all linearly independent b/c you can't form the zero vec out of any of them.  for example there's no way to change the first 1 in the x location b/c each index is only represented once with a one.
this is FOR SURE not a formal proof but regardess gets the idea across."""

#prove that any finite set T of vectors has a subset B for which B is equal to span T, using the shrink algorithm
#let the vector space V be equal to T
#def shrink(T):
#initialize B to be T
#     try taking a vector away from B, and check that you can still get span T from B:
#     keep going till you can no longer take away a vector from B and still get span T

#5.14.13
def rep2vec(u, veclist):
    """a procedure that maps a coordinate representation to its
    vector given a basis as a list of vecs a1...an"""
    basis = coldict2mat(veclist)
    return basis * u

u = list2vec([5,3,-2])
vecs = [[1,0,2,0],[1,2,5,1],[1,5,-1,3]]
veclist = [list2vec(list) for list in vecs]
outvec = rep2vec(u, veclist)
print(outvec)

#5.14.14
def vec2rep(vec, veclist):
    """a procedure that maps a vector to it's coordinate representation given a basis/set of generators
    must use solver to find the matrix that undoes the work of the matrix that originally converted from
    coordinates to vectors"""
    gens = coldict2mat(veclist)
    return solve(gens, vec)

vec = list2vec([6,-4,27,-3])
veclist = [list2vec(list) for list in [[1,0,2,0],[1,2,5,1],[1,5,-1,3]]]
print(vec2rep(vec, veclist))

#5.14.15
def is_superfluous(L, i):
    """procedure that returns True if the i'th vector is superfluous.  I.e. if the span of
    all the vectors - ith vector == span of all the vectors in L.  If the ith vector is part of the
    span of the other vecs, then it is superfluous b/c it can be formed by the others.  At that point we know that
    it's also linearly dependent.  So we test to see if there's a set of coefficients such that
    the ith vector is in the span of the others."""
    assert i <= len(L)
    if len(L) == 1: #must check to see, if L is only one vec, whether
        if L[0].f == {}:
            return True
        else:
            return False
    b = L[i]
    P = L.copy()
    P.remove(b) #must get rid of vec in question to see whether its in span of others
    A = coldict2mat(P)
    result = solve(A,b)
    residual = b - A * result
    residual_test = residual * residual
    if residual_test <= 10**-14:
        return True
    else:
        return False

def make_vecs(tests):
    tests = {key:[[list2vec(vec) for vec in value[0]],value[1]] for key,value in tests.items()}
    return tests

tests = {'t1':([[1,2,3],[1,2,3]],0), 't2':([[0,0,0,0],[0,0,0,0],[0,0,4,0]],1), 't3':([[0,0,1],[0,1,1],[1,0,0]],1)}
tests = make_vecs(tests)

def run_tests(tests): return {key:is_superfluous(value[0], value[1]) for key,value in tests.items()}

print(run_tests(tests))

#5.14.16
def is_independent(L):
    """a procedure to determine if a list of vecs is linearly independent.  We do this by testing each vector in the list to see if any of
    them is superfluous.  If they are not, then the set is linearly independent.  This is based on the Span Lemma which states that a vector creates a linear
    dependency iff it's possible to form the zero vector with a linear combination of the vectors where the vector in question has a coefficent not equal 0.  We test
    this by seeing if we can create the vector out of a linear combination of the other vectors.  If we can do this, we can 100% create the zero vector by
    taking our (linear combination of all other vecs) + -1(vector in question).  For this reason, it's sufficient to see if such a linear combination exists, which requires solving
    a linear equation."""
    super_test = [is_superfluous(L, i) for i in range(len(L))]
    if True in super_test: #if any vector is superfluous set is not linearly independent
        return False
    else:
        return True

test1 = [list2vec(l) for l in [[2,4,0],[8,16,4],[0,0,7]]]
test2 = [list2vec(l) for l in [[1,3,0,0],[2,1,1,0],[0,0,1,0],[1,1,4,-1]]]
test3 = [list2vec(l) for l in [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]]
test4 = [list2vec(l) for l in [[0,0,1],[0,1,0],[1,0,0],[1,1,1]]]
out = [is_independent(test) for test in [test1, test2, test3, test4]]
print(out)

#5.14.17
def subset_basis(T):
    """a procedure to find a basis for a set of vectors.  This is equivalent to removing all the linear dependencies, leaving only a inearly independent set that still spans.  In a
    graph situation this is equivalent to removing all the cycles, and there are multiple ways to do so.
    We start with the empty set, add a linearly independent vector from T, see if we can span T.  spanning T is equivalent to seeing if we can create all the vectors in T."""
    #create empty set
    #grab a vector at random and see if when it is added it creates a linearly independent set
        #is_independent(B)
        #if it is not, grab another vector
        #if you can't grab any other vectors, you're good, and the procedure ends .
        #this is because if you can
        #otherwise, test b to see if you can span T.
        #this is equivalent to seeing if each vector in T can be created by a linear combination of the vecs in B
        #in this context, if is_superfluous() returns True for all vectors in T added to B, you're good.
             #this is equivalent to is_independent returning false when adding all vectors in T to B .
    B = [T[0]]
    i = 0
    while True in [(is_independent(B + [t])) for t in T]: #as long as it's possible to add a vec from T that creates a linearly independent set
         if is_independent(B + [T[i]]) == True:
             B.append(T[i])
         i+=1
    return B
a0 = list2vec([1,1,1,0])
a1 = list2vec([0,1,0,0])
a2 = list2vec([0,0,1,0])
a3 = list2vec([1,0,1,0])

[print(vec) for vec in subset_basis([a0,a3,a2,a1])]

#5.14.18
def superset_basis(T,L):
    """this procedure seeks to prove the superset basis lemma, which states that for any vector space V and set of linealy indpenet vectos T,
    there is a basis for V that contains all of T.  This is actually pretty crazy once you think about it,
    because it seems like there should be a case in which adding the necessary vectors to get to V would create a linear dependency in T .
    We implement this by starting B off at T, and then repeatedly testing B to see if it spans V.  Adapted version of the Grow algorithm."""
    B = T
    i = 0
    while True in [(is_independent(B + [l])) for l in L]: #as long as span(B) != V. (i.e), as long as you can't make every vec in L with B.
         if is_independent(B + [L[i]]) == True:
             B.append(L[i])
         i+=1
    return B

T1 = [list2vec(l) for l in [[0,5,3],[0,2,2],[1,5,7]]]
L1 = [list2vec(l) for l in [[1,1,1],[0,1,1],[0,0,1]]]
T2 = [list2vec(l) for l in [[0,5,3],[0,2,2]]]
L2 = [list2vec(l) for l in [[1,1,1],[0,1,1],[0,0,1]]]

#[print(vec) for vec in superset_basis(a0,x3)]

#task 5.14.19
def exchange(S,A,z):
    """a procedure that adds a vector to a vector space and kicks out another without changing the span of the vector space.
    to do this, we set aside a linearly independent set of vecs A that is a subset of S, and make sure that we're grabbing a
    linearly independent vec z such that z + A is linearly independent.  We need to make sure that we can form w with z U A, so we will
    test z U A to try and solve for w, which must be a vector not in A but in S,and if we can, return w as a valid vector to be exchanged."""
    #assert is_independent(A + [z]) == True #make sure A + z really is independent
    #assert False not in [a in S for a in A] #make sure A is subset of S
    for w in S:
        if w not in A:
            Scopy = (S+z).copy() #im copying an array many times.  Is there a more efficient way?
            Scopy.remove(w)
            Scopy_mat = coldict2mat(Scopy)
            result = solve(Scopy_mat, w)

            #tests to make sure result valid
            residual = w - Scopy_mat * result
            residual_test = residual * residual
            if residual_test <= 10**-14:
                return w

S = [list2vec(l) for l in [[0,0,5,3],[2,0,1,3],[0,0,1,0],[1,2,3,4]]]
A = [list2vec(l) for l in [[0,0,5,3],[2,0,1,3]]]
z = [list2vec([0,2,1,1])]

print(exchange(S,A,z))
