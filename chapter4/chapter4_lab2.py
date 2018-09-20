from png import *
from matutil import listlist2mat
from image_mat_util import *
from matutil import identity as id
from mat import Mat
from math import cos, sin, pi
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
def translation(alpha, beta): return Mat(({'x','y','u'}, {'x','y','u'}),{('x','x'): 1, ('y','y'):1,('x','u'):alpha,('y','u'):beta,('u','u'):1})

print(translation(100,-200))
#mat2display(translation(3,2)*location_m, color_m)

#task 4
"""a procedure to scale an image"""
def scale(alpha,beta): return Mat((D,D),{('x','x'):alpha, ('y','y'):beta,('u','u'):1})
print(scale(4,3))
#mat2display(scale(3,2)*location_m, color_m)

#task 5
"""procedure to rotate an image"""

def rotation(rad_theta): return Mat((D,D), {('x','x'):cos(rad_theta), ('x','y'):sin(rad_theta),('y','x'):-sin(rad_theta),('y','y'):cos(rad_theta), ('u','u'):1})
print(rotation(pi/6))
#mat2display(rotation(pi/6)*location_m, color_m)

#task 6
"""rotate around a point other than the origin"""
def rotation_about(theta,x,y): return translation(x,y) * rotation(theta)
print(rotation_about((pi/2),100,-100))
#mat2display(rotation_about((pi/6),-50,50)*location_m, color_m)

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
mat2display(location_m, (grayscale() * color_m))
