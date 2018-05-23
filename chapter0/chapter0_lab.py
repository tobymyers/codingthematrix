# #0.5.1 find num of mins in week
# hour = 60
# day = 24
# week = 7
# mins_in_week = hour * day * week
# print(mins_in_week, 'num mins in week')
#
# #0.5.2 find remainder w/out %
# num_div = 2304811//43
# remainder = 2304811 - (43 * num_div)
# print(remainder, 'remainder')
#
# #0.5.3 eval boolean expression
# print(((673 + 909)//3) == 0)
#
# #0.5.4 predict value of expression with x = -9 and y = 1/2. Pred: 2 actual answer 1
# #thought that -9 + 10 was less than zero. sad
# x = -9
# y = 1/2
#
# #0.5.4 predict value of expression with x = -9 and y = 1/2. Pred: 2 actual answer 1
# #thought that -9 + 10 was less than zero. sad
# x = -9
# y = 1/2
# print(2**(y+1/2) if x + 10 < 0 else 2**(y-1/2))
# print(2**(y+1/2) if x + 10 < 0 else 2**(y-1/2))
#
# #0.5.5 write a comprehension that squares each value in {1,2,3,4,5}
# print([x**2 for x in {1,2,3,4,5}])
#
# #0.5.6 write a comprehension that raises 2 to the powers in set {0,1,2,3}
# print([2**x for x in {0,1,2,3}])
#
# #0.5.7 alter the sets used from {1,2,3} & {2,3,4} so that the image is 9 values instead of 7
# print(len([x*y for x in {1,2,3} for y in {4,5,6}]))
#
# #0.5.8 replace the sets in the comprehension from {1,2,3} and {2,3,4} so that the image is |5|
# #with non-overlapping values
# print(len({x*y for x in {0,1,2} for y in {4,8,16}}))
#
# #0.5.9 without using the intersection operator, find the intersection between two sets
# print({x for x in {1,2,3,4} if x in {3,4,5,6}})
#
# #0.5.10 write an expression whose value is the average of the list [20, 10, 15, 75]
# l = [20, 10, 15, 75]
# print(sum(l)/len(l))
#
# #0.5.11 write a double list comprehension whose output is a list containing the cartesian
# #product of ['a', 'b', 'c'] and [1,2,3]
# print([[x,y] for x in ['a', 'b', 'c'] for y in [1,2,3]])
#
# #0.5.12 write an expression that sums a bunch of lists //
# lofl = [[.25, .75, .1], [-1, 0], [4,4,4,4]]
# #print(sum([sum([x],[]) for x in lofl]), [])  almost working, syntax issue
#
# #0.5.13 find out what happens when the left side doesn't have the same || as the right side
# #[x,y,z] = [1,2,3,4] "too many values to unpack error"
#
# #0.5.14-.15-.16 write a triple comprehension such whose value is a list of 3 integer tuples that add to 0
# #and that does not include (0,0,0)
# S = {-4, -2, 1, 2, 5, 0}
# print([(i,j,k) for i in S for j in S for k in S if i+j+k == 0 and (i, j, k) != (0, 0, 0)][0])
#
# #0.5.17 find an example of a list and set with same input values but different ||
# print(len(set([1,2,2]))!=len([1,2,2]))
#
# #0.5.18 write a comprehension whose value is the set of odd numbers from 1, 99
# print([i for i in range(1,100,2)])
#
# #0.5.19 write a that combines two lists using zip and range
# L = ['a', 'b', 'c', 'd']
# print(list(zip(range(5),L)))
#
# #0.5.20 write a comprehension that sums the [nth] element of two lists
# print([x+y for (x,y) in zip ([10,25,40], [1,15,20])])
#
# #0.5.21 write a comprehension that pulls out all the values from a list of dicts that all contain that value
# dlist = [{'james': 'sean', 'director': 'terence'}, {'j':'rogers', 'director':'lewis'}, {'james':'pierce', 'director':'lewis'}, {'james': 'pierce', 'director':'roger'}]
# k = 'james'
# print([ i[k] for i in dlist if k in i]) #can filter but it doesn't like the else
#
# #0.5.23 write a dict with range where the value is squared
# print({k:k**2 for k in range(100)})
#
# #0.5.24 write a comprehension whose value is the identity frunction for some set
# d = {1,2,3,4,5}
# print({i:i for i in d})
#
# #0.5.25 write a comprehension such that given base x and integers set(range(base)) you create a
# #dict in the form 1: {0,0,1}, 2:{0,0,2}
# base = 10
# ints = set(range(base))
# #print({i:g for i in ran for g in ints }) can't figure out how to do this one, moving on
#
# #0.5.26 map names of employees to their salaries.  name[i] == i: salaries
# id2salary = {0:1000.0, 3:990, 1:1200.50}
# names = ['larry', 'curly', '', 'moe']
# print({names[i]:j for (i,j) in id2salary.items()})
#
# #0.5.28 function that outputs a list where the ith element == ith element input -1
# def plus_one(list): return [i+1 for i in list]
# print(plus_one([1,2,3]))
#
# #0.5.29 write a procedure dict2list which takes in a dict and keys and spits out proper values
# def dict2list(dict, keys): return [ dict[k] for k in keys]
# print(dict2list({'a':'A', 'b':'B', 'c':'C'},['b', 'a', 'c']) )
#
# #0.5.30 take a value list and a key list and make a dict
# def makedict(list, keys): return {l:k for (k,l) in zip (keys, list)}
# print (makedict(['a', 'b', 'c'], ['A', 'B', 'C']))
#
# #0.5.31 requires base 10--> 2 conversion.  leaving till I figure out 5.25

#0.6.1
from math import cos, log, e, pi, sqrt
print(sqrt(3), sqrt(3)**2, cos(pi), log(e))

#0.6.2
from random import randint
def review(movie): return [['truly garbage'], ['must see!'], ['what a pile of junk :)']][randint(0,2)]
print(review('ladybird'))
print(review('ladybird'))

#leaving 0.6.3-6 till I have internet

#0.6.6
def makeInverseIndex(strlist):
    split_docs = [doc.split() for doc in strlist]
    words_dict = {word:set() for doc in split_docs for word in doc}
    for word in words_dict:
        for docnum, doc in enumerate(split_docs):
            if word in doc:
                words_dict[word].add(docnum)
    return words_dict

strlist = open('stories_small.txt')
index = makeInverseIndex(strlist)
# print(index)

#0.6.7
def orSearch(inverse_index, query):
    return [inverse_index[i] for q in query.split() for i in inverse_index if q == i]
#print(orSearch(index, 'Hello, I am'))

#0.6.8
def andSearch(inverseIndex, query):
     relevant_lines = orSearch(inverseIndex, query)
     starter = set(range(1000))
     for i in relevant_lines:
         starter.intersection_update(i)
     return starter
print(andSearch(index, 'a the if though'))
