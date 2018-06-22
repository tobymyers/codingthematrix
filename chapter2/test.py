# from chapter2_vec import *
# labels = {'a', 'b', 'c', 'd', 'e'}
# function = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
# v = Vec(labels, function)
# print(v.set_item('a',5))
# print(v.get_labels())
# print(v.get_function())
# print(v.get_item('a'))
# print(v.get_item('q'))
# v2 = v.scalar_mul(2)
# print(v2.get_function())
# print(v2.get_labels())

from vec import *
v = Vec({'a', 'b', 'c'}, {'b':0})
print(v['b'])
v['a'] = 1
print(v['a'])
print(Vec({'a', 'b', 'c'}, {'a':0}) == Vec({'a', 'b', 'c'}, {'b':0}))
print(Vec({'a', 'b', 'c'}, {'a': 0}) == Vec({'a', 'b', 'c'}, {}))
print(Vec({'a', 'b', 'c'}, {}) == Vec({'a', 'b', 'c'}, {'a': 0}))
print(Vec({'x','y','z'},{'y':1,'x':2}) == Vec({'x','y','z'},{'y':1,'z':0}))
print(Vec({'a','b','c'}, {'a':0,'c':1}) == Vec({'a','b','c'}, {'a':0,'c':1,'b':4}))
print(Vec({'a','b','c'}, {'a':0,'c':1,'b':4}) == Vec({'a','b','c'}, {'a':0,'c':1}))
print(Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'b':1}))
print(Vec({'a','b'},{'a':1}) == Vec({'a','b'},{'a':2}))
