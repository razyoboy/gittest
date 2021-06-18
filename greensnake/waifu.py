import numpy as np
import random as rd
class gacha:
    count = 0
    def __init__(self, rolls):
        self.rolls = rolls

    def garuntee(self):
        for self.count in range(1, self.rolls+1):
            
            if self.count%10 == 0:
                a = "SR"
            elif self.count%100 == 0:
                a = "SSR"
            else: 
                a = "R"
            yield a
            
"""
    def RNG(self):
        b = []
        for count in range(0, self.rolls):
            self.garuntee()
            b = b.append(a) 
        return b 
"""

for value in gacha(20).garuntee():
    print(value)
       

