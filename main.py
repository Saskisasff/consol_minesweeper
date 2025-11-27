#pip install numpy
import numpy as np
from random import *
def search(x, y, check):
    global flags
    if (x, y) in bomb:
        return 0
    bombs = 0
    #UP
    if (x-1, y-1) in bomb and (x != 0):
        bombs += 1
    if (x-1, y) in bomb and (x != 0):
        bombs += 1
    if (x-1, y+1) in bomb and (x != 0):
        bombs += 1
    #DOWN
    if (x+1, y-1) in bomb and (x != 8):
        bombs += 1
    if (x+1, y) in bomb and (x != 8):
        bombs += 1
    if (x+1, y+1) in bomb and (x != 8):
        bombs += 1
    #LEFT
    if (x, y-1) in bomb and (y != 0):
        bombs += 1
    #RIGHT
    if (x, y+1) in bomb and (y != 8):
        bombs += 1
        
    if check == 1:
        if bombs == 0:
            return True
        elif bombs > 0:
            return False
        
    if bombs == 0 and (x >= 0) and (x <= 8) and (y >= 0) and (y <= 8) and check == 0:
        if a[x][y] != '/':
            a[x][y] = ' '
    else:
        if (x >= 0) and (x <= 8) and (y >= 0) and (y <= 8) and check == 0:
            if a[x][y] != '/':
                a[x][y] = str(bombs)
    
        
def field_rendering(a):
    print('\033[1;31m  0 1 2 3 4 5 6 7 8\033[0m')
    for i in range(9):
        text = ''
        text += '\033[1;31m'+str(i)+'\033[0m'
        for j in range(9):
            text += ' '
            if a[i][j] in ('1', '2', '3', '4', '5', '6', '/', '@'):
                if a[i][j] == '1':
                    text += '\033[1;34m' + a[i][j] + '\033[0m'
                elif a[i][j] == '2':
                    text += '\033[1;33m' + a[i][j] + '\033[0m'
                elif a[i][j] == '3':
                    text += '\033[1;35m' + a[i][j] + '\033[0m'
                elif a[i][j] == '4':
                    text += '\033[1;36m' + a[i][j] + '\033[0m'
                elif a[i][j] == '5':
                    text += '\033[1;37m' + a[i][j] + '\033[0m'
                elif a[i][j] == '6':
                    text += '\033[1;37m' + a[i][j] + '\033[0m'
                elif a[i][j] == '/':
                    text += '\033[1;31m' + a[i][j] + '\033[0m'
                elif a[i][j] == '@':
                    text += '\033[1;30m' + a[i][j] + '\033[0m'
                
            else:
                text += '\033[1;32m'+a[i][j]+'\033[0m'
        print(text)
        
def checking_cage(coord_x, coord_y, check):
    if check == 0:
        search(coord_x-1, coord_y-1, check)
        search(coord_x-1, coord_y, check)
        search(coord_x-1, coord_y+1, check)
        search(coord_x, coord_y-1, check)
        search(coord_x, coord_y+1, check)
        search(coord_x+1, coord_y-1, check)
        search(coord_x+1, coord_y, check)
        search(coord_x+1, coord_y+1, check)
                
a = np.full((9,9), '#')

bomb = []
flags = 10
begin = 1
for i in range(10):
    bomb.append((randint(0,8), randint(0,8)))

# for i in range(9):
#     for j in range(9):
#         if (i, j) in bomb:
#             a[i][j] = '@'
print('\033[1;31m MINESWEEPER IN CONSOLE \033[0m\n\n')
print('\033[4;37m by Saskisasff \033[0m\n')
field_rendering(a)
while True:
    print(f'Flags: {flags}')
    if flags >0:
        print('Select the mode:\no - grub\ni - to put\n')
    elif flags <= 0:
        print('Select the mode:\no - grub\n')
        if len(bomb) == 0:
            print('\033[1;32m YOU WIN! \033[0m')
            break
        else:
            print('In some places, the flags are wrong.')
            continue
    mode = input()
    if mode == 'o':
        print('Enter the x and y coordinates')
        coord_x = int(input())
        coord_y = int(input())
        if coord_x > 8 or coord_y > 8:
            print('The value is too high!')
            continue
        if coord_x < -9 or coord_y < -9:
            print('The value is too low!')
            continue
        if begin == 1:
            if (coord_x, coord_y) in bomb:
                    bomb.pop(bomb.index((coord_x, coord_y)))
                    lol = (randint(0,8), randint(0,8))
                    if lol in bomb:
                        while lol in bomb:
                            lol = (randint(0,8), randint(0,8))
                        bomb.append(lol)
                        a[bomb[-1][0]][bomb[-1][1]] = '#'
            if a[coord_x][coord_y] == '/':
                flags += 1
            a[coord_x][coord_y] = ' '
            checking_cage(coord_x, coord_y, 0)
            for i in range(9):
                for j in range(9):
                    if a[i][j] == ' ':
                        checking_cage(i, j, 0)
            field_rendering(a)
            begin = 0
            continue   
        if search(coord_x, coord_y, 1):
            if begin == 1:
                if (coord_x, coord_y) in bomb:
                    bomb.pop(bomb.index((coord_x, coord_y)))
                    bomb.append((randint(0,8), randint(0,8)))
                begin = 0
            else:
                if (coord_x, coord_y) in bomb:
                    print('\033[1;31m GAME OVER \033[0m\n\n')
                    break
            if a[coord_x][coord_y] == '/':
                flags += 1
            a[coord_x][coord_y] = ' '
            checking_cage(coord_x, coord_y, 0)
            for i in range(9):
                for j in range(9):
                    if a[i][j] == ' ':
                        checking_cage(i, j, 0)
            field_rendering(a)
        else:
            if begin == 1:
                if (coord_x, coord_y) in bomb:
                    bomb.pop(bomb.index((coord_x, coord_y)))
                    bomb.append((randint(0,8), randint(0,8)))
                begin = 0
            else:
                if (coord_x, coord_y) in bomb:
                    print('\033[1;31m GAME OVER \033[0m\n\n')
                    for i in range(9):
                        for j in range(9):
                            if (i, j) in bomb:
                                a[i][j] = '@'
                    field_rendering(a)         
                    break
            search(coord_x, coord_y, 0)
            field_rendering(a)
    elif mode == 'i' and flags > 0:
        print('Enter the x and y coordinates')
        coord_x = int(input())
        coord_y = int(input())
        if coord_x > 8 or coord_y > 8:
            print('The value is too high!')
            continue
        if coord_x < -9 or coord_y < -9:
            print('The value is too low!')
            continue
        if a[coord_x][coord_y] != '/':
            flags -= 1
        a[coord_x][coord_y] = '/'
        if (coord_x, coord_y) in bomb:
            bomb.pop(bomb.index((coord_x, coord_y)))
        field_rendering(a)