from cancer_data import *
from vecutil import *
from matutil import *

#task 1
A,b = read_training_data('train.data')
A_view = [vec for vec in mat2rowdict(A).values()]
print(coldict2mat(A_view[:10]))


#task2
def signum(u):
    return Vec(u.D, {d:-1 if u.f[d] <0 else 1 for d in u.D})


#task3
def fraction_wrong(A,b,w):
    """if all wrong, w_res == -len(b.D), if all right, len(b.D).
    bottom line moves the scale from neg len(D) --> pos len(D) to 0 ---> 2 len(D)
    """
    assert w.D == A.D[1]
    w_res = signum(A*w) * b
    return round(1 - (w_res + len(b.D))/(2*len(b.D)), 3)

w = Vec(A.D[1], {d:1 for d in A.D[1]})
l = [0.00794, -0.00283, 0.00885    ,   0.998  ,  0.999 ,0.995,  1 ,1,0.999,0.999 ,0.999 , 0.996 ,0.998  , 1, 0.998,-0.217, 0.913,-0.379,0.81,0.987,0.786, 0.997 ,  1 ,0.997,0.995,0.999,0.993,0.495,0.952,0.326]
#w = Vec(A.D[1], {d:L for (d,L) in zip(A.D[1],l)})

print(fraction_wrong(A,b,w))

#task 4
def loss(A,b,w):
     w_res = A*w
     return int((w_res - b) * (w_res - b))
print(loss(A,b,w))

#task 5 #not at all sure this is working properly
def find_grad(A,b,w):
    loss_vec = 2 * (A * w - b)
    return A.transpose() * loss_vec

print(find_grad(A,b,w))

#task 6
def gradient_descent_step(A, b, w, sigma):
    grad = find_grad(A,b,w)
    return w - (sigma * grad)

print(gradient_descent_step(A,b,w, 2* 10 ** -9))

#task 7
def gradient_descent(A, b, w, sigma, T):
    for i in range(T):
        if i%30 == 0:
            print('loss is' ,loss(A,b,w))
            print('fraction wrong is', fraction_wrong(A,b,w))
        w = gradient_descent_step(A,b,w,sigma)
    return w, w.f
sigma = 10 ** -9
print(gradient_descent(A,b,w,sigma, 100000))


#currently loss and fraction wrong are moving in opposite directions
#pretty sure fraction wrong's code is valid though, so not sure what's going on here.
#this makes me think that both loss and gradient_descent are broken
#starting with all 0 vec, both loss and fraction wrong go the same direction for awhile,
#and everything looks amazing, but then they start to diverge.
#starting with all 1 vec it starts out horrible but they move together towards lower values...this seems to be the way to do it not sure why
#will type out summary of steps later for recall practice
