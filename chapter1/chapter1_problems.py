#1.7.1 myfiter(l, num) returns list w/out list of multiples of nums
def myfilter(L, num): return [i for i in L if i%num != 0]
L = [0,1,2,3,4,5,6,7,8,9,10]
num = 2
print(myfilter(L, num))

#1.7.2 my_lists(l) for input [1,2,3], return [1], [1,2], [1,2,3]
#def my_lists(l): return [j for i in l for j in range(i)]
#print(my_lists(L)) #not right.  not returning list of lists, and incorrect for when passed 0
def my_lists(l): return [list(range(i)) for i in l]
print(my_lists(L))#fixed it!!
#1.7.3 my_function_composition(f,g): spit out g of f where g o f exists
f = {'a':1, 'b':2}
g = {1: 'one', 2: 'two'}
def my_function_composition(f, g): return {k:g[v] for (k, v) in f.items()}
print(my_function_composition(f, g))
