#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.set_brand(brand)
        self.set_size(size)
        
    def set_brand(self, brand):
        self._brand = brand
    
    def get_brand(self):
        return self._brand
    
    def set_size(self, size):
        self._size = size if isinstance(size, int) else print("size must be an integer")

    def get_size(self):
        return self._size
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    size = property(get_size, set_size)
    brand = property(get_brand, set_brand)
    