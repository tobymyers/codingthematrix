from vec import Vec
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
