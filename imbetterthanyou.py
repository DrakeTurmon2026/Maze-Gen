import turtle as turt
from random import *
import math

wn = turt.Screen()

turt.tracer(False)
man = turt.Turtle()
man.speed(0)
man.shape("square")
gridsize = 20

#made by D-Tier

colors = ["#1F3B4D","#000000"]

mazesize = (20,20)

doors = [1,3,5,7]

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
    1,1,1,
    1,1,1,
    1,1,1
]

diffrooms = [roomquad,roomtryw,roomtrye,roomtryn,roomtrys,roomcornne,roomcornnw,roomcornse,roomcornsw,roomclosed]

man.penup()
#-- FUNCS HERE --
def rendergrid(grid,onspace):
    global gridsize
    are = 0
    for tile in grid:
        man.color(colors[tile])
        man.goto((are - (math.floor(are/roomscale[0])*roomscale[1])) * gridsize + (onspace[0]*gridsize*roomscale[0]),math.floor(are/roomscale[0]) * gridsize + (onspace[1]*gridsize*roomscale[0]))
        man.stamp()
        are+=1

def Main():
    global man, roomscale


    

    
Main()

wn.mainloop()