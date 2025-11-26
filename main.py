#pip install numpy
import numpy as np
from random import *

def search(x, y):
    if (x, y) in bomb:
        return "GAME OVER"
    bombs = 0
    #UP
    if (x-1, y-1) in bomb:
        bombs += 1
    elif (x-1, y) in bomb:
        bombs += 1
    elif (x-1, y+1) in bomb:
        bombs += 1
    #DOWN
    elif (x+1, y-1) in bomb:
        bombs += 1
    elif (x+1, y) in bomb:
        bombs += 1
    elif (x+1, y+1) in bomb:
        bombs += 1
    #LEFT
    elif (x, y-1) in bomb:
        bombs += 1
    #RIGHT
    elif (x, y+1) in bomb:
        bombs += 1
    a[x][y] = bombs
        
        
        
        
a = np.full((9,9), '#')
bomb = []
for i in range(randint(4, 6)):
    bomb.append((randint(0,8), randint(0,8)))
print(bomb)
print(a)
while True:
    coord_x = int(input())
    coord_y = int(input())
    if (coord_x, coord_y) in bomb:
        bomb.pop(bomb.index((coord_x, coord_y)))
    a[coord_x+1][coord_y+1] = 0