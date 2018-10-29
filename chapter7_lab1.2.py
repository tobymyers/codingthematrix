#ran this thing all night and it only tested 1.5 million sets of vecs
#there are 64 choose 8 sets of vecs, or about 4 billion
#hacking it to only require a1,b1...a4,b4 to meet the requirement that any 6 are linearly independent
#I think this will help because a) there are now only 8 choose 6 combos, and also it's more likely that there are multiple sets of 8 6 vecs,
#compared to 10 6 vecs, that will work.
#this hurts the scheme in the sense that now it's possible that two rogue TAs, guessing the password,
#would find that there are more solutions to the matrix vector equation based on certain guesses for a0 and b0.  it still doesn't actually
#tell them the password though, unless they can form a0 and b0 out of their vecs, in which case they cannot discover the vector u but they
#can discover the correct values of s and t by forming vectors a0 and b0 from their own vectors and then using the same linear combination on their
# shares
#Ok so having thought this through, it totally messes up the scheme, but I want to try it anyway. Would still protect from 1 rogue TA.
from vecutil import *
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
    while len(map) < factorial(8)/(factorial(6) * factorial(2)):
        combo = set()
        while len(combo) < 6:
            combo.add(randint(0,7))
        map.add(tuple(combo))
    return map


#map of all combinations of 8 vectors from set of 64: 64 choose 8
def vec_combo_map():
    map = set()
    while len(map) < factorial(64)/(factorial(8) * factorial(56)):
        combo = set()
        while len(combo) < 8:
            combo.add(randint(0,63))
        map.add(tuple(combo))
        print(len(map))
    return map
print(vec_combo_map,len(vec_combo_map()), len(vec_combo_map())==factorial(64)/(factorial(8) * factorial(56)))
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
    all_6 = all_6_vecs(a0,b0)
    vectors_tried = []
    map = combo_map()
    all_independent = []
    while len(all_independent) < len(map):
        print(len(vectors_tried),'vector_combos_tried')
        all_independent = []
        ten_vecs = get_random6_vecs(all_6)# + [a0] + [b0] #+ get_standard_basis()
        vectors_tried.append(tuple(ten_vecs))
        for combo in map:
            test_vecs = get_combo(combo, ten_vecs)
            is_independent = test_independence(test_vecs)
            if is_independent == False:
                [print(vec) for vec in test_vecs]
                print(rank(test_vecs))
                break
            else:
                all_independent.append(True)
                print(len(all_independent))
                print(all_independent)
    return ten_vecs

#print(find_independent_vecs())
