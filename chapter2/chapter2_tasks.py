# #2.3.2
from plotting import *
L = [[2,2], [3,2], [1.75, 1], [2,1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]
# plot(L,4, browser ='chrome')
#
#2.4.2
def goEast(v, w): return v[0]+1, v[1]+2
print (goEast([4,4],None))
print (goEast([-4, -4],None))

#2.4.3
plot([goEast(v, [1,2] ) for v in L], 4, browser = 'chrome')

#2.4.4 write a procedure to sum two n-vectors represented as lists
def sum_vec(V, W): return [v+w for v, w in zip(V, W)]
