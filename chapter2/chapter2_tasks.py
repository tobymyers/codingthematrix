# #2.3.2
from plotting import *
L = [[2,2], [3,2], [1.75, 1], [2,1], [2.25, 1], [2.5, 1], [2.75, 1], [3, 1], [3.25, 1]]
#plot(L,6, browser ='chrome')
#
#2.4.2
def goEast(v, w): return v[0]+1, v[1]+2
print (goEast([4,4],None))
print (goEast([-4, -4],None))

#2.4.3
#plot([goEast(v, [1,2] ) for v in L], 4, browser = 'chrome')

#2.4.4 write a procedure to sum two n-vectors represented as lists
def sum_vec(V, W): return [v+w for v, w in zip(V, W)]

#2.5.3
def scale(scalar, vector): return [scalar * vector[i] for i in range(len(vector))]

#2.5.4
#plot(scale(0.5,L), 6, browser = 'chrome')

#plot(scale(-0.5,L), 6, browser = 'chrome')

#2.6.1
# w = 4/3 b/c line between 2 points == slope
#translation = f(x, y) = x+2, y+3

#2.6.2 line segment between 2 vectors 1,4 and 6, 3
#{alpha|5,-1| + |1, 4| : alpha between 0 and 1}
#check this later.
#2.6.6 tabling this proof.  made some progress and proved it out with a bunch of real numbers but proofs are
#hard AF

#2.6.9 write a procedure that lets us plot 100 points between two line segments using convex combination
def segment(u, v): #return [[u*(i/100.0)], [v]  for i,i in range(100)]
     out = []
     for i in range(100):
         up = i/100
         down = 1-i/100
         out.append([(u[0] * up )+(v[0]* down), (u[1]*up)+ (v[1] * down)])
     return out
plot(segment([3.5, 3], [0.5,1]), 6, browser = 'chrome')
