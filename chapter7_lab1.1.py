from vecutil import *
from itertools import *
from math import factorial
from independence import *
from vec import *
from mat import *
from GF2 import *
from random import randint
from matutil import *
from bitutil import *

#lab implementing a successful secret sharing scheme using vectors over GF2

#vecs a0 and b0 to be multiplied by vec u to encode 2 bit secret
a0 = list2vec([one, one, 0, one, 0, one])
b0 = list2vec([one, one, 0, 0, 0, one])
#task 7.7.1
def randGF2(): return randint(0,1) * one

def rand6vec(a0, b0):
    D = {i for i in range(6)}
    vec = Vec(D, {d:randGF2() for d in D})
    if vec != a0 and vec != b0:
        return vec
    else:
        return rand6vec(a0,b0)

def choose_secret_vector(s, t):
    """input: secret bits s and t over gf2
    output: vector u such that a0*u == s and b0*u == t
    #I'm sure there's a more elegant way to do this, but I'm generating random
    6 vecs over gf2(potential for 2**6) and testing them.  other option would be
    to solve the matrix vector equation using solver, but this reduces security"""
    a0 = list2vec([one, one, 0, one, 0, one])
    b0 = list2vec([one, one, 0, 0, 0, one])

    D = {i for i in range(6)}
    while True:
        u = rand6vec(a0, b0)
        if a0 * u == s and b0 * u == t:
            return u
#print(choose_secret_vector(a0, b0, one, 0))

#task 7.7.2 generate 8 6 vectors over GF2 such that any six vecs out of {a0,b0, other 8 vecs}
    #are linearly indpendent
#set of all 6_vecs over gf2
def all_6_vecs(a0,b0):
    l = set()
    for i in range(10000):
        l.add(rand6vec(a0,b0))
    return list(l)

#map of all combinations of 6 vectors from set of 10: 10 choose 6
def combo_map():
    map = set()
    while len(map) < factorial(10)/(factorial(6) * factorial(4)):
        combo = set()
        while len(combo) < 6:
            combo.add(randint(0,9))
        map.add(tuple(combo))
    return map


#map of all combinations of 8 vectors from set of 64: 64 choose 8
def combo_map2():
    a = all_6_vecs(a0,b0)
    assert len(a) == 62
    return combinations(a, 8)

a = combo_map2()

#gets you the vectors that correspond to a given combo
def get_combo(combo,ten_vecs):
    return [ten_vecs[i] for i in combo]

#make generator basis for gf2^6.  theory is that these will be part of solution
def get_standard_basis():
    D = {i for i in range(6)}
    v = [list2vec(l) for l in [[one, 0,0,0,0,0],[0,one,0,0,0,0],[0,0,one,0,0,0],[0,0,0,one,0,0],[0,0,0,0,0,one],[0,0,0,0,one,0]]]
    #vecs = [Vec(D, {d:one}) for d in D] for some reason doesn't like sparsity
    return v

#get 8 random 6 vecs making sure they are all unique
def get_random6_vecs(all_6_vecs):
    D = {i for i in range(6)}
    test_vecs = set()
    while len(test_vecs) < 8: #used to be <8late night change to incorporate standard basis #must ensure there are no dupe vecs, set does this naturally
         test_vecs.add(all_6_vecs[randint(0,61)])
    return list(test_vecs)

#test 6 pairs to see if they are linearly independent
def test_independence(six_vecs):
    if rank(six_vecs) == 6:
        return True
    else:
        return False

def find_independent_vecs():
    a0 = list2vec([one, one, 0, one, 0, one])
    b0 = list2vec([one, one, 0, 0, 0, one])
    fixed_vecs = (a0, b0)
    vectors_tried = []
    combos_of_six = combo_map()
    combos_of_eight = combo_map2()
    for set in combos_of_eight:
        all_ten = set + fixed_vecs
        all_independent = []
        for potential in combos_of_six:
            if rank(get_combo(potential, all_ten)) != 6:
                break
            else:
                all_independent.append(1)
                if len(all_independent) > 20:
                    print (len(all_independent))
        if len(all_independent) == 210:
            return all_ten


print(find_independent_vecs())
