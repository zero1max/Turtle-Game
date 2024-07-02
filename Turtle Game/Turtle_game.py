import turtle
import random

def rangli():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

ekran = turtle.Screen()
ekran.colormode(255)
ekran.bgcolor('black')
ekran.title("Turtle Game")

kamon = turtle.Turtle(shape='arrow')
kamon.speed(0.1)
kamon.shapesize(2)
kamon.color('white')
kamon.penup()
kamon.forward(250)
kamon.pendown()
kamon.left(90)
kamon.forward(300)
kamon.right(180)
kamon.forward(600)
kamon.penup()
kamon.right(90)
kamon.forward(520)
kamon.pendown()
kamon.right(90)
kamon.forward(600)
#----------yozuv
# S harfi
kamon.penup()
kamon.left(90)
kamon.forward(75)
kamon.pendown()
kamon.right(180)
kamon.forward(30)
kamon.right(180)
kamon.forward(30)
kamon.left(90)
kamon.forward(30)
kamon.left(90)
kamon.forward(30)
kamon.right(90)
kamon.forward(30)
kamon.right(90)
kamon.forward(30)
#--------------------
# T  harfi
kamon.penup()
kamon.left(90)
kamon.forward(90)
kamon.pendown()
kamon.left(90)
kamon.forward(30)
kamon.right(180)
kamon.forward(15)
kamon.left(90)
kamon.forward(50)
#--------------------
# A  harfi
kamon.penup()
kamon.forward(70)
kamon.pendown()
kamon.right(20)
kamon.forward(40)
kamon.right(180)
kamon.forward(40)
kamon.right(140)
kamon.forward(40)
kamon.right(180)
kamon.forward(20)
kamon.left(75)
kamon.forward(15)
kamon.penup()
kamon.left(90)
kamon.forward(70)
#--------------------
# R  harfi
kamon.pendown()
kamon.right(5)
kamon.forward(40)
kamon.right(180)
kamon.forward(40)
kamon.right(90)
kamon.forward(30)
kamon.right(90)
kamon.forward(20)
kamon.right(90)
kamon.forward(30)
kamon.left(135)
kamon.forward(30)
kamon.right(45)
kamon.penup()
kamon.forward(70)
#----------------
# T harfi
kamon.pendown()
kamon.right(90)
kamon.forward(40)
kamon.right(180)
kamon.forward(20)
kamon.right(90)
kamon.forward(40)
kamon.penup()
kamon.left(90)
kamon.forward(580)
kamon.left(90)
kamon.forward(500)
#------------------ START TUGADI!!!

# F harfi
kamon.penup()
kamon.right(90)
kamon.forward(50)
kamon.pendown()
kamon.right(90)
kamon.forward(40)
kamon.right(180)
kamon.forward(20)
kamon.right(90)
kamon.forward(30)
kamon.right(180)
kamon.forward(30)
kamon.right(90)
kamon.forward(20)
kamon.right(90)
kamon.forward(40)
kamon.right(180)
kamon.forward(40)
kamon.left(90)
kamon.forward(40)
kamon.penup()
kamon.forward(75)
#------------------
# I  harfi
kamon.left(90)
kamon.forward(20)
kamon.pendown()
kamon.right(90)
kamon.forward(40)
kamon.penup()
kamon.right(90)
kamon.forward(20)
kamon.left(90)
kamon.forward(70)
#-------------------
# N  harfi
kamon.pendown()
kamon.forward(40)
kamon.left(180)
kamon.forward(40)
kamon.right(135)
kamon.forward(50)
kamon.left(135)
kamon.forward(40)
kamon.penup()
kamon.left(180)
kamon.forward(40)
kamon.right(90)
kamon.forward(10)
kamon.left(90)
kamon.forward(50)
#-------------------
# I  harfi
kamon.pendown()
kamon.forward(40)
kamon.penup()
kamon.forward(40)
#--------------------
# S  harfi
kamon.pendown()
kamon.right(90)
kamon.forward(30)
kamon.left(90)
kamon.forward(30)
kamon.left(90)
kamon.forward(30)
kamon.right(90)
kamon.forward(30)
kamon.right(90)
kamon.forward(30)
kamon.penup()
kamon.left(90)
kamon.forward(40)
#--------------------
# H  harfi
kamon.pendown()
kamon.forward(40)
kamon.left(180)
kamon.forward(20)
kamon.right(90)
kamon.forward(20)
kamon.right(90)
kamon.forward(20)
kamon.left(180)
kamon.forward(40)
kamon.penup()
kamon.left(180)
kamon.forward(300)


#Toshbaqalar

toshbaqalar = []
hozirgi_y = -200

for i in range(10):
    toshbaqa = turtle.Turtle(shape='turtle')
    toshbaqa.color(rangli())
    toshbaqa.shapesize(2)
    toshbaqa.speed(4)
    toshbaqa.penup()
    toshbaqa.goto(-300, hozirgi_y)
    toshbaqalar.append(toshbaqa)
    hozirgi_y = hozirgi_y + 50

input()
ochilsinm = True
while ochilsinm:
    for toshbaqa in toshbaqalar:
        toshbaqa.forward(random.randint(10,60))
        if toshbaqa.xcor()>=250:
            ochilsinm = False

ekran.exitonclick()
