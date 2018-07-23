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
