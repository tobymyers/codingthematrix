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
#get_item
def get_item(v,d): return v.f[d] if d in v.f else 0
#2.7.4 add Vecs
from chapter2_vec import *
def add(Vec1, Vec2): return Vec(u.D, {d:get_item(u,d) + get_item(v, d) for d in u.D})
#this only works if these Vecs have the same domain

#2.7.5
def neg(v): return {l:-f for l,f in v.f.items()}

#2.8.4/.7 solve lights out/represent a given vector as the sum of a set of other vectors over GF(2)
#build initial state
#build button vectors
#randomly grab button vectors and add them until they equal the initial state
#report the subset that works
from chapter2_vec import *
from GF2 import *
from random import randint, randrange

def rand_state():#this works to get the inital dict of locations and a random set of 0 and 1
    l = {(i,j):randint(0,1) for i in range(5) for j in range(5)}
    for a,b in l.items():
        if b == 1:
            l[a] = one
    return l

 #this almost works, but I got frustrated trying to get rid of the out of bounds entries so using
#it to generate the main thing and then manually deleting invalid entries :0
    # bv = {(i,j):{(i,j):one, (i-1, j):one, (i+1, j):one, (i, j+1): one, (i, j-1): one} for i in range(5) for j in range(5) }
    # return bv
    #these button vecs are embarrasing but i'll fully solve it later
button_vecs = {(0, 0): {(0, 0): one, (1, 0): one, (0, 1): one },
    (0, 1): {(0, 1): one, (1, 1): one, (0, 2): one, (0, 0): one},
    (0, 2): {(0, 2): one,  (1, 2): one, (0, 3): one, (0, 1): one},
    (0, 3): {(0, 3): one, (1, 3): one, (0, 4): one, (0, 2): one},
    (0, 4): {(0, 4): one, (1, 4): one, (0, 3): one},
    (1, 0): {(1, 0): one, (0, 0): one, (2, 0): one, (1, 1): one },
    (1, 1): {(1, 1): one, (0, 1): one, (2, 1): one, (1, 2): one, (1, 0): one},
    (1, 2): {(1, 2): one, (0, 2): one, (2, 2): one, (1, 3): one, (1, 1): one},
    (1, 3): {(1, 3): one, (0, 3): one, (2, 3): one, (1, 4): one, (1, 2): one},
    (1, 4): {(1, 4): one, (0, 4): one, (2, 4): one, (1, 3): one},
    (2, 0): {(2, 0): one, (1, 0): one, (3, 0): one, (2, 1): one},
    (2, 1): {(2, 1): one, (1, 1): one, (3, 1): one, (2, 2): one, (2, 0): one},
    (2, 2): {(2, 2): one, (1, 2): one, (3, 2): one, (2, 3): one, (2, 1): one},
    (2, 3): {(2, 3): one, (1, 3): one, (3, 3): one, (2, 4): one, (2, 2): one},
    (2, 4): {(2, 4): one, (1, 4): one, (3, 4): one, (2, 3): one},
    (3, 0): {(3, 0): one, (2, 0): one, (4, 0): one, (3, 1): one },
    (3, 1): {(3, 1): one, (2, 1): one, (4, 1): one, (3, 2): one, (3, 0): one},
    (3, 2): {(3, 2): one, (2, 2): one, (4, 2): one, (3, 3): one, (3, 1): one},
    (3, 3): {(3, 3): one, (2, 3): one, (4, 3): one, (3, 4): one, (3, 2): one},
    (3, 4): {(3, 4): one, (2, 4): one, (4, 4): one, (3, 3): one},
    (4, 0): {(4, 0): one, (3, 0): one,(4, 1): one },
    (4, 1): {(4, 1): one, (3, 1): one,  (4, 2): one, (4, 0): one},
    (4, 2): {(4, 2): one, (3, 2): one,  (4, 3): one, (4, 1): one},
    (4, 3): {(4, 3): one, (3, 3): one, (4, 4): one, (4, 2): one},
    (4, 4): {(4, 4): one, (3, 4): one, (4, 3): one}}

def solve():
    state = rand_state()
#add button vectors until I find one that == s 
