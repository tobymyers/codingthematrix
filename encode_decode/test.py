# from encode import *
# l = encode("i think I can I think")
# print(l.text_to_binary())
#
# a = {0:0, 1:0, }
# for (i,j) in a.items():
#     print(i, j)
#     print(encode.gf2add(i, j))

from key import *
k = Key(10000)
print(k.get_length())
k.save()
from text import *
t = Text('test_file.py', 'key_instance.py')
t.to_gf2()
print(t.encode())
