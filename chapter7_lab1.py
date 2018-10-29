from vecutil import *
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

#get 8 random 6 vecs making sure they are all unique
def get_random6_vecs(all_6_vecs):
    D = {i for i in range(6)}
    test_vecs = set()
    while len(test_vecs) < 8: #must ensure there are no dupe vecs, set does this naturally
         test_vecs.add(all_6_vecs[randint(0,61)])
    return test_vecs

#format vectors as pairs format {1:{'a':Vec, 'b':Vec}, 2:....}
def pair_format(test_vecs):
    list_vecs = list(test_vecs)
    return {i:{'a':list_vecs[i], 'b':list_vecs[i+1]} for i in range(1,5)}

#add formatted vecs to a0 and b0
def add_a0_b0(test_vecs, a0, b0):
    ab = {'a':a0,'b':b0}
    test_vecs[0] = ab
    return test_vecs

#grab 3 pairs from dict_set
def grab_3_pairs(dict_vecs):
    rand3 = set()
    while len(rand3) < 3:
        rand3.add(randint(1,4))
    return {i:dict_vecs[i] for i in rand3}



#test 3 pairs to see if they are linearly independent
def test_independence(threepairs):
    pairs = [pair for pair in threepairs.values()]
    vecs = [vec for pair in pairs for vec in pair.values()]
    if rank(vecs) == len(vecs):
        return True
    else:
        return False

def make_mat(threepairs):
    pairs = [pair for pair in threepairs.values()]
    vecs = [vec for pair in pairs for vec in pair.values()]
    return rowdict2mat(vecs)

s,t = one, 0
all_6_vecs = all_6_vecs(a0,b0)
def sharer(s,t, a0,b0,all_6_vecs):
    u = choose_secret_vector(s,t)
    count = 0
    true_for_all = False
    while true_for_all != [True] * 1000:
        test_vecs = get_random6_vecs(all_6_vecs)
        dict_vecs = pair_format(test_vecs)
        five_pairs = add_a0_b0(dict_vecs,a0,b0)
        count+= 1
        #print(count)
        true_for_all = []
        for i in range(1000):
            random3 = grab_3_pairs(five_pairs)
            is_independent = test_independence(random3)
            if is_independent == False:
                print('False')
                break
            else:
                print('True')
                true_for_all.append(is_independent)
    return five_pairs

TA_mat = sharer(one, 0, a0,b0, all_6_vecs)
print(TA_mat)

#optional: putting it all together
#actually sharing  string and putting it back together

string = "wrist"
def get_U_from_str(string):
    bits = str2bits(string)
    mat = bits2mat(bits,2)
    sts = [(vec.f[0],vec.f[1]) for vec in mat2coldict(mat).values()]
    u_vecs = [choose_secret_vector(st[0],st[1]) for st in sts]
    U = coldict2mat(u_vecs)
    return U
