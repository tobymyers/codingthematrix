from vec import Vec
from image_mat_util import *
from mat import Mat
from solver import solve
from matutil import *
from vecutil import list2vec
#task 1
def move2board(y_vec):
    """function that maps the location of a point in the whiteboard plane not
    on the whiteboard to a point on the white board such that the line from the origin
    through the y_vec will intersect the whiteboard at the output point
    input must be a 'y1','y2','y3' vector.
    would have liked a more general function but I guess there's no situation where this
    applies where the labels aren't defined."""
    #return Vec(y_vec.D, {y_vec.D[0]:y_vec.D[0]/y_vec.D[2],y_vec.D[1]:y_vec.D[1]/y_vec.D[2], y_vec.D[2]:1})
    y3 = y_vec
    assert y_vec.D == {'y1', 'y2', 'y3'}
    return Vec(y_vec.D, {k:v/y_vec.f['y3'] for k,v in y_vec.f.items()})
v = Vec({'y1','y2','y3'}, {'y1':5, 'y2':3, 'y3':0.5})
print(move2board(v))


#task 2
D = {(y,x) for y in ['y3','y2','y1'] for x in ['x1','x2','x3']}
def make_equations(w1, w2, x1, x2):
    """this prodedure returns the vectors that if multiplied by the unknown values in H would produce 0, hence giving us opportunity
    to solve for the values of H.  Could use solver to do it but that so far has not been part of the lab.  This procedure is in service of converting from the camera basis to the
    whiteboard basis."""
    u = Vec(D, {('y3','x1'):w1*x1, ('y3', 'x2'):w1*x2, ('y3','x3'):w1, ('y1','x1'):-x1, ('y1', 'x2'):-x2, ('y1', 'x3'):-1})
    v = Vec(D, {('y3','x1'):w2*x1, ('y3', 'x2'):w2*x2, ('y3','x3'):w2, ('y2','x1'):-x1, ('y2', 'x2'):-x2, ('y2', 'x3'):-1})
    return [u,v]
    #return [Vec((D),{'d:l for d,l in zip(D,[w1*x1, w1*x2, w1, -x1, -x2, -1])}),Vec((D),{d:l for d,l in zip(D,[w2*x1, w2*x2, w2, -x1, -x2, -1])})]


print(make_equations(2,4,6,8))

#task 3
"""D vector to set the scale of H, b/c a hypothetical H that satisfied all linear equations
would still work if it was scaled up by some scalar a.  This would result in an image of any size and reflects the fact that
the camera in the whiteboard basis could be either really close to the whiteboard or very far away"""
w = Vec(D,{('y1','x1'):1})

#task 4
corner_map = {'tl':[0,0,358,36],'bl':[0,1,329,597],'tr':[1,0,592,157],'br':[1,1,580,483]}
e = [make_equations(k[0],k[1],k[2],k[3]) for k in corner_map.values()]
vecs = []
[vecs.extend(i) for i in e]
vecs.append(w)
L = rowdict2mat(vecs)
print(L)

b = Vec({i for i in range(9)}, {8:1})
print(b)
h = solve(L,b)
print(h)
residual = (b - (L * h) )
print (residual * residual) #something isn't working here with my matrix.  currently doesn't have a solution, but the pieces are in place.
#checked functons f and u, checked order of inputs to make_equations.

H = Mat(({'y1','y2','y3'},{'x1','x2','x3'}),h.f)
print(H)

#task 5
(X_pts, colors) = file2mat('board.png',('x1','x2','x3'))

#task 6
Y_pts = H * X_pts#takes 1-2 mins to process
print(Y_pts.D[1],Y_pts.D[0])

#task 7
def mat_move2board(Y):
    """at this stage we've mapped image coordinates to whiteboard coordinates in the image
    now we need to map those whiteboard coordinates to the whiteboard plane itself.  this is basically saying
    that we haven't yet "spun" the image so that the whiteboard plane was parallel to the plane of the paper"""
    y_vecs = mat2coldict(Y)
    return coldict2mat({p:move2board(y) for (p,y) in y_vecs.items()})

Y_board = mat_move2board(Y_pts)
print(type(Y_board),  Y_board.D[0])
#task 8
mat2display(Y_board, colors, ('y1','y2','y3'),scale = 100, xmin= None, ymin = None)
