from vec import *
#quiz 1.4.1
L = [[0] * 4 for i in range(3)]
A = [[0 for j in range(4)] for i in range(3)]
print(A)
print(L)

#quiz 1.4.2
L = [[i-j for i in range(3)] for j in range(4)]
print(L)

#quiz 4.1.4 give a Vec with the above matrix
#Vec({'a','b'}, {'a':3, 'b':30})

#quiz 4.1.5 coldict representation of dictionary
"""Vec({'a', 'b'}, {'a':1, 'b':10})
Vec({'a', 'b'}, {'a':2, 'b':20})
Vec({'a', 'b'}, {'a':3, 'b':30})"""

#4.1.7
#M = Mat(({'a','b','c'}, {'a', 'b', 'c'}), {('a','a'):1, ('b','b'):1, ('c','c'):1})

#4.1.8
class Mat:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function
    def print(self):
        return self.D, self.f
def identity(labels): return Mat(({labels}, {labels}), {(l1, l2):1 for l1 in labels for l2 in labels if l1 == l2}).print()
print(identity(('a','b','c')))
