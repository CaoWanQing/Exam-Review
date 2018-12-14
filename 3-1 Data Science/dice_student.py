# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 15:23:36 2016

@author: zhengzhang
"""

constant = 100
import random
import dice_helper

class Dice:
    def __init__(self, sides=6):
        self.n_sides = sides
        self.bounds = [x/sides for x in range(0, sides)]
        self.bounds.append(1.0)
        self.point = None
        self.lands = 0

    def set_bounds(self, r):
        assert len(r) == len(self.bounds)
        self.bounds = r

    def get_bounds(self):
        return self.bounds

    def roll(self):
        num = random.random()
        # if size 6,
        #return 0, 1, 2, 3, 4, 5
        #if size = n, return 0, or, 1, or 2, or ... n-1

        # loop through each interval, see if num is in it
        for i in range(len(self.bounds)):
            if self.bounds[i] <= num < self.bounds[i+1]:
                return i




if __name__ == "__main__":
    d = Dice()
    ''' make a biased dice '''
    d.set_bounds([0.0, 0.3, 1.0])
    ones = 0
    num_rolls = 1000
    for i in range(num_rolls):
        ones += d.roll()
    print("the dice is:", ones/float(num_rolls))

in_circle = 0
# n time
n = 1000
for i in range(n):
    # generate (x, y)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # check if in_circle
    dist = (x ** 2 + y ** 2)** 0.5
    if dist <= 1:
        in_circle += 1

# calculate pi
pi = 4 * in_circle / n
