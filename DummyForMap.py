import time
import random
import numpy as np

def nextmove(lastmove, arena, xpos, ypos):
    if (lastmove == 0): #utara
        if (xpos-1 != -1): #barat
            if (arena[ypos][xpos-1] == 0):
                return 3
        if (ypos-1 != -1): #utara
            if (arena[ypos-1][xpos] == 0):
                return 0
        if (xpos+1 != 15): #timur
            if (arena[ypos][xpos+1] == 0):
                return 1
        if (ypos+1 != 9): #selatan
            if (arena[ypos+1][xpos] == 0):
                return 2
        return 5 #backtrack
    elif (lastmove == 1): #timur
        if (ypos-1 != -1): #utara
            if (arena[ypos-1][xpos] == 0):
                return 0
        if (xpos+1 != 15): #timur
            if (arena[ypos][xpos+1] == 0):
                return 1
        if (ypos+1 != 9): #selatan
            if (arena[ypos+1][xpos] == 0):
                return 2
        if (xpos-1 != -1): #barat
            if (arena[ypos][xpos-1] == 0):
                return 3
        return 5 #backtrack
    elif (lastmove == 2): #selatan
        if (xpos+1 != 15): #timur
            if (arena[ypos][xpos+1] == 0):
                return 1
        if (ypos+1 != 9): #selatan
            if (arena[ypos+1][xpos] == 0):
                return 2
        if (xpos-1 != -1): #barat
            if (arena[ypos][xpos-1] == 0):
                return 3
        if (ypos-1 != -1): #utara
            if (arena[ypos-1][xpos] == 0):
                return 0
        return 5 #backtrack
    else: #barat
        if (ypos+1 != 9): #selatan
            if (arena[ypos+1][xpos] == 0):
                return 2
        if (xpos-1 != -1): #barat
            if (arena[ypos][xpos-1] == 0):
                return 3
        if (ypos-1 != -1): #utara
            if (arena[ypos-1][xpos] == 0):
                return 0
        if (xpos+1 != 15): #timur
            if (arena[ypos][xpos+1] == 0):
                return 1
        return 5 #backtrack
    
myarena = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0 - 14
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 15 - 29
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 30 - 44
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 45 - 59
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 60 - 74
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 75 - 89
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 90 - 104
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 105 - 119
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 120 - 134
]
xpos = 0
ypos = 0
lastaction = 1

while(lastaction != 5):
    action = nextmove(lastaction, myarena, xpos, ypos)
    if (action == 0):
        ypos -= 1
        myarena[ypos][xpos] = 1
    elif (action == 1):
        xpos += 1
        myarena[ypos][xpos] = 1
    elif (action == 2):
        ypos += 1
        myarena[ypos][xpos] = 1
    elif (action == 3):
        xpos -= 1
        myarena[ypos][xpos] = 1
    lastaction = action
    time.sleep(5)