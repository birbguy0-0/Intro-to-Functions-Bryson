import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(1000)

# for i in range(3):
#     print(i)

# for i in range(4):
#     t.forward(100)
#     t.left(90)

# for i in range(60):
#     t.forward(200)
#     t.left(90)
#     t.forward(200)
#     t.left(90)
#     t.forward(200)
#     t.left(90)
#     t.forward(200)
#     t.left(5)

#VARIABLES

# sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
# square(100,90)

# def doubleSquares(iRange):
#     length = 25
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 2
# doubleSquares(5)

# def addSquares(iRange):
#     length = 5
#     for i in range(iRange):
#         square(length, 90)
#         length += 5
#         t.right(5)
# addSquares(60)


def star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)

def addStars(iRange):
    length = 5
    for i in range(iRange):
        star(length, 144)
        length += 5
        t.right(5)
addStars(60)


turtle.done()