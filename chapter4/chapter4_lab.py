from matutil import listlist2mat, mat2coldict, coldict2mat
from vec import *
from mat import *
from GF2 import *
from bitutil import *
#task 4.14.1
G = Mat(({0,1,2,3,4,5,6}, {0,1,2,3}), {(0,0):one, (0,1):0, (0,2):one, (0,3):one, (1,0):one, (1,1):one, (1,2):0, (1, 3):one, (2,0):0, (2,1):0, (2,2):0, (2, 3):one, (3,0):one, (3,1):one, (3,2):one, (3, 3):0, (4,2):one, (5,1):one, (6,0):one})
print(G)

G1 = G.transpose()
print(G1)

#task 4.14.2 encode [one, 0, 0, one]
p = Vec({0,1,2,3},{0:one, 3: one})
print(p, "p")
c = G*p

#4.13.3 going from codewords to words
#because rows a, b, and d of g are parity bits, and we dont need them to go
#from codewords to words b/c we already checked against H, a,b and d can be all
#zeros.  this leaves us with a 4x4 identity matrix

R = listlist2mat([[0,0,0,0,0,0,one],[0,0,0,0,0,one,0],[0,0,0,0,one,0,0],[0,0,one,0,0,0,0]])
print("R",R)
print("R*c",R*c)
print("R*G", R*G)


#4.14.4 Decoding
#In my head I calulated that p = [0000] for [0111100]*G because four of the
#rows of G are standard generators for gf2^4, (positions 3 5 6 and 7), any codeword with a 1 there
#will evaulate to a 1 in the linear combination step.  The other three rows have 3 ones, don't know what that means
#^^this note from day before is super interesting. I was sooo close just didnt' understand what a parity bit was :).  They are just tests to make sure other bits have not been corrupted.  what happpens if parity bits get corrupted?
#in this case the normal bits act as parity bits for the parity bits themselves :)

#4.14.3 built a 4x7 matrix R such that, for any codeword c, the matrix vector prodct R*c equals
#ANGER!  this seems impossible, b/c non square matrices aren't invertible. if it was however, it seems
#thinking that I don't understand this question

#4.14.4
H = Mat(({0,1,2},{0,1,2,3,4,5,6}), {(0,3):one,(0,4):one, (0,5):one, (0,6):one,  (1,1):one, (1,2):one, (1,5):one, (1,6):one, (2,0):one, (2,2):one, (2,4):one, (2,6):one})
print(H)
print(H*G) #it IS the 0 matrix, bc this must be the case to recognize the error?  also because any word passed through G
#would become a codeword which when multiplied by the H vector must evaluate to 0
#what's cool about this is that H somehow represents all the potential codewords, even though I have yet to pass anything through it

#4.14.5 procedure that returns error syndrome
def find_error(e):
    pos = sum([2**(2-i) for i in e.f.keys() if e.f[i] == one]) - 1
    if pos < 0:
        return Vec({0,1,2,3,4,5,6},{})
    else:
        return  Vec({0,1,2,3,4,5,6},{pos:one})


def find_error1(c_codeword):
    error_vec = H*c_codeword
    error_list = [i for i in error_vec.f.values()]
    new_items = [x if x==0 else 1 for x in error_list]
    error_str = ''.join(map(str, new_items))
    error_location = int(error_str,2) -1  #matrix is 0 indexed
    error_vec = Vec({0,1,2,3,4,5,6},{})
    error_vec[error_location]= one
    return error_vec

def find_error2(error_vec):
    error_list = [i for i in error_vec.f.values()]
    new_items = [x if x==0 else 1 for x in error_list]
    error_str = ''.join(map(str, new_items))
    error_location = int(error_str,2) -1  #matrix is 0 indexed
    error_vec = Vec({0,1,2,3,4,5,6},{})
    error_vec[error_location] = one
    return error_vec

#4.14.6 given corrupted codeword find original message
cc = Vec({0,1,2,3,4,5,6},{0:one, 2:one, 3:one, 5:one, 6:one})
e = find_error(cc)
c = cc - e
print(H*c, "H*c")
p = R * c
print(cc, 'cc', e, 'e', G*p, 'G*p')
print(p)

#4.14.7 find_error_matrix
def find_error_matrix(S):
    return coldict2mat({v:find_error(mat2coldict(S)[v]) for v in mat2coldict(S).keys()})
#     ss= mat2coldict(S)
#     s = [find_error2(syndrome) for syndrome in ss.values()]
#     return coldict2mat(s)
# S = listlist2mat([[one, 0],[one,0],[one,one]])
# print(find_error_matrix(S), 's')

#4.14.7 putting it all together
s= ''.join([chr(i) for i  in range(256)])
#print(s)
#4.14.8
#print(bits2str(str2bits(s)))

#4.14.9
b = str2bits(s)
P = bits2mat(b)
a = mat2bits(P)
#print(P)
#print(a)
#print(bits2str(a))

#4.14.10
s ="""’Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe.

“Beware the Jabberwock, my son!
      The jaws that bite, the claws that catch!
Beware the Jubjub bird, and shun
      The frumious Bandersnatch!”

He took his vorpal sword in hand;
      Long time the manxome foe he sought—
So rested he by the Tumtum tree
      And stood awhile in thought.

And, as in uffish thought he stood,
      The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
      And burbled as it came!

One, two! One, two! And through and through
      The vorpal blade went snicker-snack!
He left it dead, and with its head
      He went galumphing back.

“And hast thou slain the Jabberwock?
      Come to my arms, my beamish boy!
O frabjous day! Callooh! Callay!”
      He chortled in his joy.

’Twas brillig, and the slithy toves
      Did gyre and gimble in the wabe:
All mimsy were the borogoves,
      And the mome raths outgrabe. """
P = bits2mat(str2bits(s))
C = G * P
#print(A)

#4.14.11
CTILDE = C + noise(C, 0.02)
#print(bits2str(mat2bits(S)))

#4.14.12
#3/7ths more after encoding

#4.14.13
corrupt = R * CTILDE

#4.14.14
def correct(L):
    return find_error_matrix(H*L)+L

words = correct(CTILDE)
print(bits2str(mat2bits(corrupt)),'corrupt')
print(bits2str(mat2bits(R*words)), 'Hamming-ed')
