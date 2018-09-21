from png import *
from matutil import listlist2mat
from image_mat_util import *
from matutil import identity as id
from mat import Mat
from math import cos, sin, pi, atan2
D = {'x','y','u'}
#task 1
"""turn image into matrices with file2mat"""
matrices = file2mat('/Users/tobymyers/Desktop/matrix/chapter4/my_bike.png')
color_m = matrices[1]
location_m = matrices[0]
#mat2display(location_m, color_m)

#task 2
"""make an identity matrix for location vectors"""
def identity(): return id({'x','y','u'},1)
print( identity()* location_m== location_m) #test identity on points
#mat2display((identity()* location_m),color_m) #test identity on image

#task 3
"""a procedure to translate an image"""
def translate(alpha, beta): return Mat(({'x','y','u'}, {'x','y','u'}),{('x','x'): 1, ('y','y'):1,('x','u'):alpha,('y','u'):beta,('u','u'):1})

#location_m = translation(300,300) * location_m
print(translate(100,-200))
#mat2display(translation(3,2)*location_m, color_m)

#task 4
"""a procedure to scale an image"""
def scale(alpha,beta): return Mat((D,D),{('x','x'):alpha, ('y','y'):beta,('u','u'):1})
print(scale(4,3))
#mat2display(scale(3,2)*location_m, color_m)

#task 5
"""procedure to rotate an image"""
#rotation function is broken, need to fix later, but plan for general reflection should be good.
def rotation(rad_theta): return Mat((D,D), {('x','x'):cos(rad_theta), ('x','y'):sin(rad_theta),('y','x'):-sin(rad_theta),('y','y'):cos(rad_theta), ('u','u'):1})
print(rotation(pi/2),"rotation")
#mat2display(rotation(pi)*location_m, color_m)

#task 6
"""rotate around a point other than the origin"""
def rotation_about(theta,x,y): return translate(x,y) * rotation(theta)
print(rotation_about((0),200,200))
print("rotation about")

#mat2display(rotation_about((3*pi/2),200,200)*location_m, color_m)

#task 7
"""reflect around the y axis"""
def reflect_y(): return Mat((D,D),{('x','x'):-1,('y','y'):1, ('u','u'):1})
print(reflect_y())
#mat2display(reflect_y()*location_m, color_m)

#task 8
"""reflect around the x axis"""
def reflect_x(): return Mat((D,D),{('x','x'):1,('y','y'):-1, ('u','u'):1})
#mat2display(reflect_x()*location_m, color_m)

#task 9
"""scale colors"""
cD = {'r','g','b'}
def scale_color(r,g,b): return Mat((cD,cD),{('r','r'):r,('g','g'):g,('b','b'):b})
print(scale_color(2,3,4))
#print(location_m,(scale_color(1,2,3) * color_m))
#mat2display(location_m,(scale_color(1,2,3) * color_m))

#task 10
"""convert to greyscale"""
def grayscale():
    a = Mat((cD,cD),{})
    for r in cD:
        for c,v in zip(cD,[(77/256),(151/256),(28/256)]):
            a[r,c] = v
    return a
print(grayscale())
#mat2display(location_m, (grayscale() * color_m))

#task 11
"""general reflection around a line defined by two points"""
def reflect_about(x1,y1,x2,y2):
    rad_theta = atan2((y2-y1),(x2-x1)) #need to convert slope to radians
    line_avg_x, line_avg_y = (y1+y2)/2, (x1+x2)/2
    top_x,top_y = location_m.f[('x',(0,0))], location_m.f[('y',(0,0))]
    trans_m = translate(line_avg_x-top_x, line_avg_y-top_y) * location_m
    spun_trans_m = rotation(rad_theta) * trans_m
    reflect_spun_trans_m = reflect_x() * spun_trans_m
    unspun_trans_m = rotation(-rad_theta) * reflect_spun_trans_m
    untrans_m = translate(line_avg_x - top_x , line_avg_y-top_y) * unspun_trans_m
    mat2display(untrans_m, color_m)

#location_m = rotation(pi/4) * location_m
location_m = translate(10,10) * location_m
reflect_about(100,100,105,105)
reflect_about(20,21,21,20)
