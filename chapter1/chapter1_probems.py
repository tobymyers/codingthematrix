#1.7.1 myfiter(l, num) returns list w/out list of multiples of nums
def myfilter(L, num): return [i for i in L if i%num != 0]
L = [0,1,2,3,4,5,6,7,8,9,10]
num = 2
print(myfilter(L, num))

#1.7.2 my_lists(l) for input [1,2,3], return [1], [1,2], [1,2,3]
def my_lists(l): return [ [range(i)] for i in l]
print(my_lists(L))
