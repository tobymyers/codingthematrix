#7.9.3
from matutil import rowdict2mat
from vecutil import *
from GF2 import *
def is_echelon(A):
    """takes in matrix as list of row lists and returns True if matrix is in echelon
    form, False otherwise"""
    first_non0s = []
    for a in A:
        first_non0 = [col for (col,val) in enumerate(a) if val !=0][0]
        first_non0s.append(first_non0)
    current = -1
    for non0 in first_non0s:
        if non0 <= current:
            return False
        current = non0
    return True
test1 = [[2,1,0],[0,-4,0],[0,0,1]]
test2 = [[2,1,0],[-4,0,0],[0,0,1]]
test3 = [[2,1,0],[0,3,0],[1,0,1]]
test4 = [[1,1,1,1,1],[0,2,0,1,2],[0,0,0,5,3]]
[print(is_echelon(test)) for test in [test1, test2, test3, test4]]

#7.9.6 echelon_solve
def echelon_solve(row_list, label_list, b):
    """proud of this one.  figured it out very much by trial and error,
    and still would be hard to describe it to a friend, but it works!  key insights:
    the column of the input vector being updated matches i.  sets are not to be trusted for order,
    hence label set as an input.  the triangular solve works b/c it is
    a square so you i == j by definition in an upper triangular context
    """
    D = row_list[0].D
    n = len(D)
    x = zero_vec(D)
    for j in reversed(range(len(row_list))):
        i = [i for i in label_list if row_list[j].f[i] != 0][0]
        if i != []:
            x[i] = (b[j] - row_list[j] * x)/row_list[j][i]
    return x



D = ['A','B','C','D','E']
test1 = [Vec(set(D),{k:v for (k,v) in zip(D,l)}) for l in [[one, 0, one, one, 0], [0, one, 0,0, one],[0,0,one, 0,one],[0,0,0,0,one]]]
b1 = [one, 0, one, one]
label_list = ['A','B','C','D','E']
print(echelon_solve(test1, label_list ,b1))

#7.9.7
#pass the rows of M, [ABCD], and M * g == 1100
