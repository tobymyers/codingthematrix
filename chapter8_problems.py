#8.3.15
from independence import *
from matutil import *
from vecutil import *
def projection_matrix(v):
    m = coldict2mat([v]) * rowdict2mat([v])
    v = 1/(v*v)
    return m * v

v = list2vec([1,3,5,6])
a = projection_matrix(v)
print(projection_matrix(v) * list2vec([2,1,4,51]))
b = list2vec([1,2,3])
c = coldict2mat([b]) * rowdict2mat([b])
print(c)
#8.3.16

"""rank must be == 1 because you're multiplying v * vT, so every column in M is a scaled
version of v.  Therefore, any row or column in a can be formed by a linear combo of v,
or any other column/row in v.  therefore by the definition of linear indpendence, dim is 1, and rank is one"""

#8.3.17
"""
for an n vector v and an nXn matrix M, to compute M*v you must complete n**2 scalar multiplications.  This is because
M is made of v*v.t(), so it's gotta be square.  by the dot product def of Mv mult, to compute a single value j of
the output vec you must do n scalar mults.  there are n rows in M, so n*n, so n**2."""

"""b) because each row and column of M is a scaled up version of v (i,e totally linearly dependent),
instead of multiplying M*v you could instead multiply mi(any row of m) * v, and then build your matrix
by using the first column of M as a set of scalars.  Essentially you're breaking M down into the row and column
vecs you used to create it and doing the multiplication one step at a time. this only works if you count each scalar vec mult as 1, which i
don't know if you can"""
