class encode:

    def __init__(self, plaintext):
        self.plain = plaintext

    def text_to_binary(self ):
        self.binary =  [int(bin(ord(i))[2:]) for i in self.plain]
        return self.binary

    def gf2add(our_bin, key_bin):
        if not our_bin + key_bin == 2:
            return our_bin + key_bin
        else:
            return 0
    # 
    # def binary_to_cypher(self, key):
    #     self.cypher = [gf2add(i, //correct index of key// for i in chr for chr in self.binary]
