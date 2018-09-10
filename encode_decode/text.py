from GF2 import *
import ast
class Text:
    def __init__(self, file, key_instance):
        """a text object that can convert plaintext to cyphertext and back"""
        self.file = open(str(file), 'r')
        self.key = open(str(key_instance), 'r')

    def to_gf2(self):
        chr_list = [word for line in self.file for word in line for chr in word] # ['7','y']
        bin = [format(ord(i), 'b') for i in chr_list] #['00001','0101']
        bin_list = [chr for str in bin for chr in str] #['0','1','0']
        for chr in range(len(bin_list)):
            if bin_list[chr] == '1':
                    bin_list[chr] = one
            else:
                bin_list[chr] = int(bin_list[chr])
        self.gf2_plain = bin_list
        return self.gf2_plain #[0, one, 0]

    def encode(self):  #NEED TO MOVE THE BULLSHIT AROUND READING IN FROM A FILE TO THE TOP,
    #THAT WAY I W=-0
        """takes plaintext and converts itself to pcyphertext """
        key_list = self.key.read()
        key_list = key_list.split(', ')[1:-1]# ['7','y']
        for key in range(len(key_list))
            if key_list[key] == '1':
                key_list[key] = one
            else:
                key_list[key] = 0
        self.cypher = [k+int(p) for (k,p) in zip(self.gf2_plain, key_list)]

        return self.cypher, len(self.cypher), 'cypherlen', len(self.gf2_plain), 'gf2'

    def decode(self):
        """takes cyphertext and converts itself to plaintext"""
        pass

    def save(self):
        """saves text object as new file with same name, erasing old version?"""
        pass
