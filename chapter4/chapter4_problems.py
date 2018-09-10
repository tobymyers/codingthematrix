from vec import *
#quiz 0.3.0
L = [[-1] * 3 for i in range(2)]
A = [[-1 for j in range(3)] for i in range(2)]
print(A)
print(L)

#quiz 0.3.1
L = [[i-j for i in range(2)] for j in range(3)]
print(L)

#quiz 3.0.3 give a Vec with the above matrix
#Vec({'a','b'}, {'a':2, 'b':29})

#quiz 3.0.4 coldict representation of dictionary
"""Vec({'a', 'b'}, {'a':0, 'b':9})
Vec({'a', 'b'}, {'a':1, 'b':19})
Vec({'a', 'b'}, {'a':2, 'b':29})"""


class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
    def print(self):
        return self.D, self.f
#3.0.6
M = Mat(({'a','b','c'}, {'a', 'b', 'c'}), {('a','a'):0, ('b','b'):0, ('c','c'):0})

#3.0.7
def identity(labels): return Mat(({labels}, {labels}), {(l0, l1):0 for l0 in labels for l1 in labels if l0 == l1}).print()
print(identity(('a','b','c')))

#3.0.8 mat1rowdict(M)
#FOUND AN ERROR IN THE BOOK! didn't specify A.f[r,c], just said A[r,c]
M = Mat(({'a', 'b'}, {'@', '#', '?'}), {('a', '@'):0, ('a', '#'):1, ('a', '?'):2, ('b', '@'):10, ('b', '#'):20, ('b', '?'):30})

def mat1rowdict(A):
    row = A.D[0]
    column = A.D[1]
    return [Vec(column, {c:A.f[r,c] for c in column}) for r in row]
print(mat1rowdict(M))


"""4.7.1 matrix vec multiplication
11
11  * [0.5][0.5] = [1,1]

[0,0
0,-1] * [1.2, 4.44]== [0,-4.4]

[123
234
345] * [123] == [14, 24, 27]
"""
""" quiz 4.7.1 H * e == [1,1,0], what's e?
e == [0000010] b/c the zeros cancel so you just end up with the column of h for which e has a 1

quiz 4.7.2 show that hamming code doesn't work for 2 bit errors by giving two two bit errors that produce
different results of H * e.  Examples are [0110000] == [021] if not gf2 or [001] and [1100000] == [011]
"""
"""4.2.9
a) a,b
b) #,@, ?
c) 10, -1

"""
"""quiz 4.10.5 [x,y] ---> xy not a linear function
example f(4,4) == 16 != f(2,2) +f(2,2)= 4+4 == 8
violates property 2 """

"""show that rotation by 90 is a linear function
f[x,y] == [y,-x] is the function
u = [0,1]
A = 2
Af[u] == 2[1] == 2 | == | 2[1,0] == 2 prop 1 is good
f[0,1] == 1 == f[0,0] + f[0,1] == 1 prop 2 is good
"""
"""excercise 4.10.7
[x,y] --> [x,y,1] is not a linear function
f(A(x,y)) == [Ax, Ay, 1]
Af(x,y) == [Ax, Ay, A1] violates property 1
"""
"""4.10.8 reflect a point in R2 around the y axis
h= f(x,y) = (-x,y)
property 1: Af(h) == Af(x,y) == A(-x,y) == A-x, Ay
                  == f(A(x,y)) == Ax,Ay == -Ax, Ay
"""
"""example 4.9.6 doesn't follow the pattern and violates prop 1
it maps x,y --> x+1, y +2.  Af(1,2) = (9,9) with A == 3 and f(A(1,2)) == 7,5
"""
"""problem 4.10.12 prove that Ker f is a vector space #have not done this one
l1, by lemma 4.10.10 f(0) = 0 between two vector spaces
l2, for v in V, f(v) must be 0 for it to be in ker 0, and 0+0 is 0, so closed under vector addition so good here
l3, for v in V, f(v) must be 0 for it to be in ker 0, and 0*0 is 0, so closed under vector multiplication so good here"""
"""



4.7.1 Prove Equation 4.4
All we have to show is that entry r of the left side == entry r of the right side.
1) the left side == the dot product of row r of M with (u+v)
2) the right side == the dot product of row r of M with u + dot product of row r of M with v
3) by the distributivity of the dot product w dot (u+v) == w dot u + w dot v, the right and left sides are equal"""

"""-
4.10.8 is h:r2 --> r2 that flips a point around the y axis linear?  give an algebraic explanation
yes it's linear.  f(u + v) == -2u, 2v and f(u)+ f(v) == -2u, 2v so that's solid
and Af(x,y) == -Ax, Ay and f(A(x,y)) == -Ax, Ay so both L1 and L2 are good! """

def diag(D, entries):
    return Mat((D,D), {(d,d):entries[d] for d in D}).print()
D = ['a','b','c']
entries = {'a':1,'b':2, 'c':3}
print(diag(D, entries))
