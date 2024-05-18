import numpy as np
#import matplotlib.pyplot as plt
import random

# Arena Assignment
arenamove = [[[0 for i in range(4)] for j in range(30)] for k in range(18)]
arena = [[0 for i in range(30)] for j in range(18)]
movepair = [2, 3, 0, 1]
xpos = 0
ypos = 0
arena[ypos][xpos] = 1
lastaction = 1
for i in range(18):
    for j in range(30):
        if (i == 0):
            arenamove[i][j][0] = 6
        if (i == 17):
            arenamove[i][j][2] = 6
        if (j == 0):
            arenamove[i][j][3] = 6
        if (j == 29):
            arenamove[i][j][1] = 6

# Reinforcement Learning
def searchzero(arena, arenamove, xpos, ypos):
    # Hyperparameter dan Q Table
    Qtable = [[0 for i in range(4)] for i in range(540)]
    learningrate = 0.1
    discountrate = 1.0
    explorationrate = 0.1
    episode = 200
    maxstep = 300
    movement = [0, 1, 2, 3]
    doit = False
    # rpe = []
    # spe = []
    
    # Training
    for i in range(episode):
        state = xpos + 30*ypos
        newypos = ypos
        newxpos = xpos
        reward = -1
        #total_reward = 0
        total_step = 0
        
        while True:
            # Eksplorasi dan eksploitasi
            if (random.uniform(0, 1) < explorationrate):
                myaction = random.choice(movement)
            else:
                myaction = np.argmax(Qtable[state])
            
            # Mengubah posisi state
            if (arenamove[newypos][newxpos][myaction] == 0 or arenamove[newypos][newxpos][myaction] == 1):  
                if (myaction == 0):
                    newypos -= 1
                elif (myaction == 1):
                    newxpos += 1
                elif (myaction == 2):
                    newypos += 1
                else:
                    newxpos -= 1  
            else:
                reward -= 10

            # Update Q table
            newstate = newxpos + 30*newypos
            if (arena[newypos][newxpos] == 0):
                reward += 10
            oldvalue = Qtable[state][myaction]
            nextvalue = max(Qtable[newstate])
            newvalue = (1-learningrate)*oldvalue + learningrate*(reward + discountrate*nextvalue)
            Qtable[state][myaction] = newvalue
            state = newstate
            
            #total_reward += reward
            total_step += 1
            
            # Tujuan tercapai atau meencapai maxstep
            if (arena[newypos][newxpos] == 0 or total_step == maxstep):
                break
        #rpe.append(total_reward)
        # spe.append(total_step)
        
    # grafik jumlah reward
    # plt.title("cumulative reward per episode")
    # plt.xlabel("Episode")
    # plt.ylabel("cumulative reward")
    # plt.plot(rpe)
    # plt.show()

    # # grafik jumlah tindakan
    # plt.title("# steps per episode")
    # plt.xlabel("Episode")
    # plt.ylabel("# steps")
    # plt.plot(spe)
    # plt.show()    
        
    # Eksploitasi untuk mengeluarkan output pergerakan backtracking
    changexpos = xpos
    changeypos = ypos
    outputmovement = []
    step = 0
    while (not doit):
        statenow = changexpos + 30*changeypos
        goaction = np.argmax(Qtable[statenow])
        if (goaction == 0):
            changeypos -= 1
        elif (goaction == 1):
            changexpos += 1
        elif (goaction == 2):
            changeypos += 1
        elif (goaction == 3):
            changexpos -= 1
        outputmovement.append(goaction)
        step += 1
        if (arena[changeypos][changexpos] == 0):
            doit = True
        if (step == maxstep):
            outputmovement = "reject"
            doit = True
            
    return(outputmovement)

# Left Spiral
def nextmove(lastmove, arena, arenamove, xpos, ypos):
    if (lastmove == 0): #atas
        if (arena[ypos][xpos-1] == 0 and xpos != 0):
            if (arenamove[ypos][xpos][3] == 0):
                return 3
        if (arena[ypos-1][xpos] == 0 and ypos != 0):
            if (arenamove[ypos][xpos][0] == 0):
                return 0
        if (xpos != 29):
            if (arena[ypos][xpos+1] == 0):
                if (arenamove[ypos][xpos][1] == 0):
                    return 1
        if (ypos != 17):
            if (arena[ypos+1][xpos] == 0):
                if (arenamove[ypos][xpos][2] == 0):
                    return 2
        return 5
    elif (lastmove == 1): #kanan
        if (arena[ypos-1][xpos] == 0 and ypos != 0):
            if (arenamove[ypos][xpos][0] == 0):
                return 0
        if (xpos != 29):
            if (arena[ypos][xpos+1] == 0):
                if (arenamove[ypos][xpos][1] == 0):
                    return 1
        if (ypos != 17):
            if (arena[ypos+1][xpos] == 0):
                if (arenamove[ypos][xpos][2] == 0):
                    return 2
        if (arena[ypos][xpos-1] == 0 and xpos != 0):
            if (arenamove[ypos][xpos][3] == 0):
                return 3
        return 5
    elif (lastmove == 2): #bawah
        if (xpos != 29):
            if (arena[ypos][xpos+1] == 0):
                if (arenamove[ypos][xpos][1] == 0):
                    return 1
        if (ypos != 17):
            if (arena[ypos+1][xpos] == 0):
                if (arenamove[ypos][xpos][2] == 0):
                    return 2
        if (arena[ypos][xpos-1] == 0 and xpos != 0):
            if (arenamove[ypos][xpos][3] == 0):
                return 3
        if (arena[ypos-1][xpos] == 0 and ypos != 0):
            if (arenamove[ypos][xpos][0] == 0):
                return 0
        return 5
    else: #kiri
        if (ypos != 17):
            if (arena[ypos+1][xpos] == 0):
                if (arenamove[ypos][xpos][2] == 0):
                    return 2
        if (arena[ypos][xpos-1] == 0 and xpos != 0):
            if (arenamove[ypos][xpos][3] == 0):
                return 3
        if (arena[ypos-1][xpos] == 0 and ypos != 0):
            if (arenamove[ypos][xpos][0] == 0):
                return 0
        if (xpos != 29):
            if (arena[ypos][xpos+1] == 0):
                if (arenamove[ypos][xpos][1] == 0):
                    return 1
        return 5

# Ultrasonic Sensor
# ganti disini
def lookfront(lastaction):
    global arena, ypos, xpos
    if (lastaction == 0):
        return arena[ypos-1][xpos]
    if (lastaction == 1):
        return arena[ypos][xpos+1]
    if (lastaction == 2):
        return arena[ypos+1][xpos]
    if (lastaction == 3):
        return arena[ypos][xpos-1]
    
def lookright(lastaction):
    global arena, ypos, xpos
    if (lastaction == 0):
        return arena[ypos][xpos+1]
    if (lastaction == 1):
        return arena[ypos+1][xpos]
    if (lastaction == 2):
        return arena[ypos][xpos-1]
    if (lastaction == 3):
        return arena[ypos-1][xpos]
    
def lookleft(lastaction):
    global arena, ypos, xpos
    if (lastaction == 0):
        return arena[ypos][xpos-1]
    if (lastaction == 1):
        return arena[ypos-1][xpos]
    if (lastaction == 2):
        return arena[ypos][xpos+1]
    if (lastaction == 3):
        return arena[ypos+1][xpos]
    
def lookbehind(lastaction):
    global arena, ypos, xpos    
    if (lastaction == 0):
        return arena[ypos+1][xpos]
    if (lastaction == 1):
        return arena[ypos][xpos-1]
    if (lastaction == 2):
        return arena[ypos-1][xpos]
    if (lastaction == 3):
        return arena[ypos][xpos+1]

# Cek sekitar
def checkaround(movepart, lastaction):
    if (lastaction == 0):
        if (movepart[0] == 0):
            movepart[0] = lookfront(lastaction)
        if (movepart[1] == 0):
            movepart[1] = lookright(lastaction)
        if (movepart[2] == 0):
            movepart[2] = lookbehind(lastaction)
        if (movepart[3] == 0):
            movepart[3] = lookleft(lastaction)
    if (lastaction == 1):
        if (movepart[0] == 0):
            movepart[0] = lookleft(lastaction)
        if (movepart[1] == 0):
            movepart[1] = lookfront(lastaction)
        if (movepart[2] == 0):
            movepart[2] = lookright(lastaction)
        if (movepart[3] == 0):
            movepart[3] = lookbehind(lastaction)
    if (lastaction == 2):
        if (movepart[0] == 0):
            movepart[0] = lookbehind(lastaction)
        if (movepart[1] == 0):
            movepart[1] = lookleft(lastaction)
        if (movepart[2] == 0):
            movepart[2] = lookfront(lastaction)
        if (movepart[3] == 0):
            movepart[3] = lookright(lastaction)
    if (lastaction == 3):
        if (movepart[0] == 0):
            movepart[0] = lookright(lastaction)
        if (movepart[1] == 0):
            movepart[1] = lookbehind(lastaction)
        if (movepart[2] == 0):
            movepart[2] = lookleft(lastaction)
        if (movepart[3] == 0):
            movepart[3] = lookfront(lastaction)

# Dummy Arena
arena = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0],
         [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6]]

# Bergerak
while True:
    action = nextmove(lastaction, arena, arenamove, xpos, ypos)
    if (action == 0):
        arenamove[ypos][xpos][action] = 1
        ypos -= 1
        arena[ypos][xpos] = 1
        arenamove[ypos][xpos][movepair[action]] = 1
    elif (action == 1):
        arenamove[ypos][xpos][action] = 1
        xpos += 1
        arena[ypos][xpos] = 1
        arenamove[ypos][xpos][movepair[action]] = 1
    elif (action == 2):
        arenamove[ypos][xpos][action] = 1
        ypos += 1
        arena[ypos][xpos] = 1
        arenamove[ypos][xpos][movepair[action]] = 1
    elif (action == 3):
        arenamove[ypos][xpos][action] = 1
        xpos -= 1
        arena[ypos][xpos] = 1
        arenamove[ypos][xpos][movepair[action]] = 1
    else:
        backtrack = searchzero(arena, arenamove, xpos, ypos)
        if (backtrack == "reject"):
            break
        else:
            for i in backtrack:
                if (i == 0):
                    arenamove[ypos][xpos][i] = 1
                    ypos -= 1
                    arena[ypos][xpos] = 1
                    arenamove[ypos][xpos][movepair[i]] = 1
                elif (i == 1):
                    arenamove[ypos][xpos][i] = 1
                    xpos += 1
                    arena[ypos][xpos] = 1
                    arenamove[ypos][xpos][movepair[i]] = 1
                elif (i == 2):
                    arenamove[ypos][xpos][i] = 1
                    ypos += 1
                    arena[ypos][xpos] = 1
                    arenamove[ypos][xpos][movepair[i]] = 1
                else:
                    arenamove[ypos][xpos][i] = 1
                    xpos -= 1
                    arena[ypos][xpos] = 1
                    arenamove[ypos][xpos][movepair[i]] = 1
                checkaround(arenamove[ypos][xpos], i)
                action = i
    lastaction = action
    checkaround(arenamove[ypos][xpos], lastaction)
for i in arena:
    print(i)