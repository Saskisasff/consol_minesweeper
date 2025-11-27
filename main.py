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
# for i in range(9):
#     for j in range(9):
#         if (i, j) in bomb:
#             a[i][j] = '@'
# print(bomb)
print('\033[1;31m MINESWEEPER IN CONSOLE \033[0m')
print('\033[4;37m by Saskisasff \033[0m')
print("\033[1;32;40m\n")
print(a)
while True:
    print('Select the mode:\no - grub\ni - to put\n')
    mode = input()
    if mode == 'o':
        print('Enter the x and y coordinates')
        coord_x = int(input())
        coord_y = int(input())
        if (coord_x, coord_y) in bomb:
            bomb.pop(bomb.index((coord_x, coord_y)))
        a[coord_x][coord_y] = '-'
        search(coord_x-1, coord_y-1)
        search(coord_x-1, coord_y)
        search(coord_x-1, coord_y+1)
        search(coord_x, coord_y-1)
        search(coord_x, coord_y+1)
        search(coord_x+1, coord_y-1)
        search(coord_x+1, coord_y)
        search(coord_x+1, coord_y+1)
        print(a)
    elif mode == 'i':
        print('Enter the x and y coordinates')
        coord_x = int(input())
        coord_y = int(input())
        if (coord_x, coord_y) in bomb:
            a[coord_x][coord_y] = '/'
            print('ВЕРНО')
        else:
            print('НЕВЕРНО')