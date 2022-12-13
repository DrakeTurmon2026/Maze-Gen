import turtle as turt
from random import *
import math

wn = turt.Screen()
wn.setup(1.0,1.0)

turt.tracer(False)
man = turt.Turtle()
man.speed(0)
man.shape("square")
gridsize = 20
isfirstroom = True

#made by D-Tier

colors = ["#155ca3","#000000"]

doors = [1,3,5,7]
connected = [7,5,3,1]
offset = [[0,-1],[-1,0],[1,0],[0,1]]

hasgened = []
togenerate = []

roomscale = [3,3]
roomquad = [
    1,0,1,
    0,0,0,
    1,0,1
]
roomtryw = [
    1,0,1,
    1,0,0,
    1,0,1
]
roomtryn = [
    1,1,1,
    0,0,0,
    1,0,1
]
roomtrys = [
    1,0,1,
    0,0,0,
    1,1,1
]
roomtrye = [
    1,0,1,
    0,0,1,
    1,0,1
]
roomcornne = [
    1,1,1,
    0,0,1,
    1,0,1
]
roomcornnw = [
    1,1,1,
    1,0,0,
    1,0,1
]
roomcornse = [
    1,0,1,
    0,0,1,
    1,1,1
]
roomcornsw = [
    1,0,1,
    1,0,0,
    1,1,1
]
roomclosed = [
    0,0,0,
    0,0,0,
    0,0,0
]
hall1 = [
    1,1,1,
    0,0,0,
    1,1,1
]
hall2 = [
    1,0,1,
    1,0,1,
    1,0,1
]

diffrooms = [roomquad,roomtryw,roomtrye,roomtryn,roomtrys,roomcornne,roomcornnw,roomcornse,roomcornsw,hall1,hall2]

def randroomid():
    return randint(0,len(diffrooms)-1)

man.penup()
#-- FUNCS HERE --
def rendergrid(grid,onspace):
    global gridsize, roomscale
    are = 0
    for tile in grid:
        if tile == 1:
            man.goto((are - (math.floor(are/roomscale[0])*roomscale[1])) * gridsize + (onspace[0]*gridsize*roomscale[0]),math.floor(are/roomscale[0]) * gridsize + (onspace[1]*gridsize*roomscale[0]))
            man.stamp()
        are+=1

def getroomexits(grid):
    done = []
    for i,ex in enumerate(doors):
        if grid[ex] == 0:
            done.append(i)
    return done

def genroom(entranceid,space):
    global man, roomscale
    #anti regen stuff
    for pos in hasgened:
        if space == pos:
            togenerate.pop(0)
            return False

    #do stuff early to prevent regens
    hasgened.append(space)
    togenerate.pop(0)
    newroom = diffrooms[randroomid()]
    print(entranceid)
    while True:
        if newroom[entranceid] == 0:
            break
        else:
            newroom = diffrooms[randroomid()]
    rendergrid(newroom,space)
    toappend = getroomexits(newroom)
    for id in toappend:
        should = True
        for pos in hasgened:
            if [space[0] + offset[id][0], space[1] + offset[id][1]] == pos:
                should = False
                break
        if should:
            togenerate.append([space,offset[id],connected[id]])

def Main():
    global isfirstroom
    if isfirstroom:
        the = diffrooms[randroomid()]
        rendergrid(the,[0,0])
        hasgened.append([0,0])
        varnamehere = getroomexits(the)
        for available in varnamehere:
            togenerate.append([[0,0],offset[available],connected[available]])
        isfirstroom = False
    else:
        if len(togenerate) > 0:
            done = len(togenerate)
            #if done > 5:
            #    done = 5
            for i in range(done):
                current = togenerate[0]
                nexpos = [current[0][0] + current[1][0], current[0][1] + current[1][1]]
                genroom(current[2], nexpos)
    
    wn.ontimer(Main,1)

wn.bgcolor("#155ca3")

Main()
wn.mainloop()
