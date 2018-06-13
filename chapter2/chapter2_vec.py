#the book says I should just write procedures that take a Vec instance as an input.  I'm going to write them as methods.
class Vec:

    def __init__(self, labels, function):
        self.D = labels
        self.f = function

    def get_labels(self): return self.D

    def get_function(self): return self.f

    def set_item(self, label, value):
        self.f[label] = value

    def get_item(self, label): return self.f[label] if label in self.f else None

    def scalar_mul(self, scalar):
        """this one is a bit weird b/c it creates a new Vec with a new function"""
        new_f = {k:scalar * v for k,v in self.f.items() if v != 0}
        print(new_f)
        return Vec(self.D, new_f)

     
