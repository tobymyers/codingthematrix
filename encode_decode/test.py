from encode import *
l = encode("i think I can I think")
print(l.text_to_binary())

a = {0:0, 1:0, }
for (i,j) in a.items():
    print(i, j)
    print(encode.gf2add(i, j))
