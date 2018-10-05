from vec import *
from vecutil import list2vec
from mat import *
from matutil import *
#quiz 0.3.0
L = [[-1] * 3 for i in range(2)]
A = [[-1 for j in range(3)] for i in range(2)]
print(A)
print(L)

#quiz 0.3.1
L = [[i-j for i in range(2)] for j in range(3)]
print(L)

#quiz 3.0.3 give a Vec with the above matrix
#Vec({'a','b'}, {'a':2, 'b':29})

#quiz 3.0.4 coldict representation of dictionary
"""Vec({'a', 'b'}, {'a':0, 'b':9})
Vec({'a', 'b'}, {'a':1, 'b':19})
Vec({'a', 'b'}, {'a':2, 'b':29})"""


#3.0.6
M = Mat(({'a','b','c'}, {'a', 'b', 'c'}), {('a','a'):0, ('b','b'):0, ('c','c'):0})

#3.0.7
def identity(labels): return Mat(({labels}, {labels}), {(l0, l1):0 for l0 in labels for l1 in labels if l0 == l1}).print()

#3.0.8 mat1rowdict(M)
#FOUND AN ERROR IN THE BOOK! didn't specify A.f[r,c], just said A[r,c]
M = Mat(({'a', 'b'}, {'@', '#', '?'}), {('a', '@'):0, ('a', '#'):1, ('a', '?'):2, ('b', '@'):10, ('b', '#'):20, ('b', '?'):30})

def mat1rowdict(A):
    row = A.D[0]
    column = A.D[1]
    return [Vec(column, {c:A.f[r,c] for c in column}) for r in row]
print(mat1rowdict(M))


"""4.7.1 matrix vec multiplication
11
11  * [0.5][0.5] = [1,1]

[0,0
0,-1] * [1.2, 4.44]== [0,-4.4]

[123
234
345] * [123] == [14, 24, 27]
"""
""" quiz 4.7.1 H * e == [1,1,0], what's e?
e == [0000010] b/c the zeros cancel so you just end up with the column of h for which e has a 1

quiz 4.7.2 show that hamming code doesn't work for 2 bit errors by giving two two bit errors that produce
different results of H * e.  Examples are [0110000] == [021] if not gf2 or [001] and [1100000] == [011]
"""
"""4.2.9
a) a,b
b) #,@, ?
c) 10, -1

"""
"""quiz 4.10.5 [x,y] ---> xy not a linear function
example f(4,4) == 16 != f(2,2) +f(2,2)= 4+4 == 8
violates property 2 """

"""show that rotation by 90 is a linear function
f[x,y] == [y,-x] is the function
u = [0,1]
A = 2
Af[u] == 2[1] == 2 | == | 2[1,0] == 2 prop 1 is good
f[0,1] == 1 == f[0,0] + f[0,1] == 1 prop 2 is good
"""
"""excercise 4.10.7
[x,y] --> [x,y,1] is not a linear function
f(A(x,y)) == [Ax, Ay, 1]
Af(x,y) == [Ax, Ay, A1] violates property 1
"""
"""4.10.8 reflect a point in R2 around the y axis
h= f(x,y) = (-x,y)
property 1: Af(h) == Af(x,y) == A(-x,y) == A-x, Ay
                  == f(A(x,y)) == Ax,Ay == -Ax, Ay
"""
"""example 4.9.6 doesn't follow the pattern and violates prop 1
it maps x,y --> x+1, y +2.  Af(1,2) = (9,9) with A == 3 and f(A(1,2)) == 7,5
"""
"""problem 4.10.12 prove that Ker f is a vector space #have not done this one
l1, by lemma 4.10.10 f(0) = 0 between two vector spaces
l2, for v in V, f(v) must be 0 for it to be in ker 0, and 0+0 is 0, so closed under vector addition so good here
l3, for v in V, f(v) must be 0 for it to be in ker 0, and 0*0 is 0, so closed under vector multiplication so good here"""
"""



4.7.1 Prove Equation 4.4
All we have to show is that entry r of the left side == entry r of the right side.
1) the left side == the dot product of row r of M with (u+v)
2) the right side == the dot product of row r of M with u + dot product of row r of M with v
3) by the distributivity of the dot product w dot (u+v) == w dot u + w dot v, the right and left sides are equal"""

"""-
4.10.8 is h:r2 --> r2 that flips a point around the y axis linear?  give an algebraic explanation
yes it's linear.  f(u + v) == -2u, 2v and f(u)+ f(v) == -2u, 2v so that's solid
and Af(x,y) == -Ax, Ay and f(A(x,y)) == -Ax, Ay so both L1 and L2 are good! """

def diag(D, entries):
    return Mat((D,D), {(d,d):entries[d] for d in D}).print()
D = ['a','b','c']
entries = {'a':1,'b':2, 'c':3}

#4.17.13
def lin_comb_mat_vec_mult(M,v):
    """multiplies a matrix by a vector using only v[k] and the linear combination definition"""
    assert M.D[1] == v.D #make sure columns of matrix == d of vector
    out_vec = Vec(M.D[0],{}) #make a blank vector with the rows of the Vector
    col_dict = mat2coldict(M) #turn the matrix into a dict format 0: vec, 1, vec
    #now grab a value from the in-vec and a vec from the matrix
    #multiply the vec value by every value in the matrix and update the value of the matrix with the new value
    #after doing this for each value in the matrix, go through and add each matrix vec value with matching domain
    #spit out result of this
    for (vec_label,mat_col) in zip(v.D,col_dict.values()):
        for col_label in mat_col.D:
            mat_col[col_label] = v[vec_label] * mat_col[col_label]
    row_dict = mat2rowdict(coldict2mat(col_dict))
    for (vec_label, row) in zip(out_vec.D,row_dict.values()):
            out_vec[vec_label] = sum([row.f[val] for val in row.D])

    return out_vec
M = listlist2mat([[2,4],[6,8]])
v = Vec({0,1},{0:2,1:2})

#print(lin_comb_mat_vec_mult(M,v))

#4.17.4 procedure to do vector matrix multiplication with only getitem
#should be basically reverse of 4.17.3
def lin_comb_vec_mat_mult(v,M):
    assert M.D[0] == v.D #make sure columns of matrix == d of vector
    out_vec = Vec(M.D[1],{}) #make a blank vector with the rows of the Vector
    col_dict = mat2rowdict(M) #turn the matrix into a dict format 0: vec, 1, vec
    #now grab a value from the in-vec and a vec from the matrix
    #multiply the vec value by every value in the matrix and update the value of the matrix with the new value
    #after doing this for each value in the matrix, go through and add each matrix vec value with matching domain
    #spit out result of this
    for (vec_label,mat_col) in zip(v.D,col_dict.values()):
        for col_label in mat_col.D:
            mat_col[col_label] = v[vec_label] * mat_col[col_label]
    row_dict = mat2coldict(rowdict2mat(col_dict))
    for (vec_label, row) in zip(out_vec.D,row_dict.values()):
            out_vec[vec_label] = sum([row.f[val] for val in row.D])
    return out_vec

def lin_comb_vec_mat_mult2(v,M):
    M = M.transpose()
    return lin_comb_mat_vec_mult(M,v)

print(lin_comb_vec_mat_mult(v,M))
print(lin_comb_vec_mat_mult2(v,M))

#4.17.15 dot product mat_vec_mult using only dot product
def dot_product_mat_vec_mult(M,v):
    assert M.D[1] == v.D
    row_vecs = mat2rowdict(M)
    out_vec = Vec(M.D[0],{})
    for (row,d) in zip(row_vecs.values(),v.D):
        out_vec[d] = v * row
    return out_vec
print(dot_product_mat_vec_mult(M,v),'mat_vec')

#4.17.16 dot product vec_mat_mult using only dot product
def dot_product_vec_mat_mult(v,M):
    assert M.D[0] == v.D
    col_vecs = mat2coldict(M)
    out_vec = Vec(M.D[1],{})
    for (col,d) in zip(col_vecs.values(),v.D):
        out_vec[d] = v * col
    return out_vec
print(dot_product_vec_mat_mult(v,M),'dot vec_mat')

#4.17.17 raw mat_vec mul using just the * operator
def Mv_mat_mat_mul(A,B):
    #is it cheating if it says I can only use the * operator?
    return A*B

A = listlist2mat([[0,1],[2,3]])
B = listlist2mat([[3,4],[5,7]])
print(Mv_mat_mat_mul(A,B))

def vM_mat_mat_mul(A,B):
    return A*B

#4.17.18 UN voting data
def create_voting_dict(strlist):
    dic = {string[0]:string[3:-1] for string in strlist}
    for key, val in dic.items():
        ints = [int(str) for str in val]
        dic[key] = ints
    return dic

file = open('UN_voting_data.txt')
mylist =[(line.split(' ')) for line in file]

def data2mat(str_list):
    voting_dict = create_voting_dict(str_list)
    #convert to a dict form 'country': Vec(0,1...n, {votes})
    country_vecs = {country:list2vec(votes) for (country,votes) in voting_dict.items()}
    return coldict2mat(country_vecs)
    #use rowdict2mat to convert into matrix
# a = data2mat(mylist)
# dot_a = a.transpose() * a
# dot_a_vecs = mat2coldict(dot_a)
# print(dot_a)
#4.17.20
def dictlist_helper(dlist,k): return[dict[k] for dict in dlist for key,value in dict.items() if key == k ]

dlist = [{'a':'apple','b':'bug'},{'a':2,'b':7},{'a':5,'b':9}]
k = 'a'

print(dictlist_helper(dlist,k))

m = listlist2mat([[4,1,-3],[2,2,-2]])
print(m.transpose())

#4.17.23 find an invertible function that can't be represented by a matrix
#what about f(x) = x^2?  
