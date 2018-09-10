#1.7.1 myfiter(l, num) returns list w/out list of multiples of nums
def myfilter(L, num): return [i for i in L if i%num != 0]
L = [0,1,2,3,4,5,6,7,8,9,10]
num = 2
print(myfilter(L, num))

#1.7.2 my_lists(l) for input [1,2,3], return [1], [1,2], [1,2,3]
#def my_lists(l): return [j for i in l for j in range(i)]
def my_lists(l): return [list(range(i)) for i in l]
print(my_lists(L))#fixed it!!
#1.7.3 my_function_composition(f,g): spit out g of f where g o f exists
f = {'a':1, 'b':2}
g = {1: 'one', 2: 'two'}
def my_function_composition(f, g): return {k:g[v] for (k, v) in f.items()}
print(my_function_composition(f, g))

#1.7.3 sum a list
def summer(l):
    current = 0
    for i in l:
        current = current + i
    return current
#1.7.4
def product(l):
    current = 0
    for i in l:
        current = current * i
    return current
#1.7.5
def my_min(l):
    current = ''
    for i in l:
        if i < current:
            current = i
    return current
#1.7.7
def my_concat(l):
    current = ''
    for i in l:
        current = current + i
    return current

#1.7.8
def my_union(listofsets):
    current = listofsets[1]
    for set in listofsets:
        current = current | set
    return current
print(my_union([{1},{2,1}, {5,4}]))

#1.7.9
#1 empty set
#2 empty set
#3 empty set
#4 empty string
#5 empty set
#5b you end up with union and intersection being the exact same things

#1..7.10
#a (5+3j)
#b (1j)
#c (-1 + 0.001j)
#d (0.001 + 9j)

#1.7.11
#a e**3j
#b e**(11pi/12)i
c# still working here

#1.7.13
#a 1
#b 0
#c 0
