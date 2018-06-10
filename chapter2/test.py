from chapter2_vec import *
labels = {'a', 'b', 'c', 'd', 'e'}
function = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
v = Vec(labels, function)
print(v.set_item('a',5))
print(v.get_labels())
print(v.get_function())
print(v.get_item('a'))
print(v.get_item('q'))
v2 = v.scalar_mul(2)
print(v2.get_function())
print(v2.get_labels())
