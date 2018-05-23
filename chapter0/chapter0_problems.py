#0.8.1:
def increments(l): return[ i+1 for i in l]
print(increments([1,4,6]), [1,4,6])

#0.8.2
def cubes(l): return [i**3 for i in l]
print(cubes([1,4,6]),[1,4,6])

#0.8.3 #not working
# def tuple_sum(A,B): return []
# A = [(1, 2), (10, 20)]
# B = [(3,4), (30,40)]
# print(tuple_sum(A, B), A, B)

#0.8.4 reverse dict
def reverse_dict(dict): return {y:x for (x,y) in dict.items()}
print(reverse_dict({'hi':'hola', 'thanks':'gracias'} ))

#0.8.6 Yes, it's invertible, because it is one-to-one and onto

#0.8.7 No, not invertible, b/c it's not onto.  there are values in the co-domain that don't exist in teh domain
#I to make it invertible, put a fifth dot in u

#0.8.8 domain = R+ would make this defined.  Otherwise -1 and 1 would both go to sqrt(1), making this not invertible.  Still don't
#eally know what defined means in the context of this.  co-domain would be R+ as well.

#0.8.9 yes, it is defined.  the co-domain of f is a valid domain for g

#0.8.10
#P(even) = 0.7 and P(odd) = 0.3

#0.8.11
#gotta figure out Mod first
