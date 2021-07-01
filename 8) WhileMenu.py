#Import libraries
import turtle
from time import sleep
import ctypes
user32 = ctypes.windll.user32

#Generate drawing environment
t=turtle.Pen()

#Tab to turtle window after first shape
def singleTab():
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)    
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt
    

#Setting up start position function
def startPosition():
    xAxis=int(input("Where would you like to start on the X axis?\n"))
    yAxis=int(input("Where would you like to start on the Y axis?\n"))
    t.up()
    t.setx(xAxis)
    t.sety(yAxis)
    t.down()

#Setting up function to draw a square
def drawASquare():
    sideLength=int(input("How long, in inches, would you like each side?\n"))
    singleTab()
    t.fd(96*sideLength)
    t.lt(90)
    t.fd(96*sideLength)
    t.lt(90)
    t.fd(96*sideLength)
    t.lt(90)
    t.fd(96*sideLength)
    t.lt(90)
    t.up()
    t.home()
    t.down()
    singleTab()

#Setting up function to draw a triangle
def drawATriangle():
    sideLength=int(input("How long, in inches, would you like each side?\n"))
    singleTab()
    t.lt(60)
    t.fd(96*sideLength)
    t.rt(120)
    t.fd(96*sideLength)
    t.rt(120)
    t.fd(96*sideLength)
    t.lt(180)
    t.up()
    t.home()
    t.down()
    singleTab()

#Setting up function to draw a rocket
def drawARocket():
    sideLength=int(input("How long,in inches, would you like the side of the rocket to be?\n"))
    singleTab()
    t.fd(48*sideLength)
    t.lt(90)
    t.fd(96*sideLength)
    t.circle(24*sideLength,180)
    t.lt(90)
    t.fd(48*sideLength)
    t.rt(180)
    t.fd(48*sideLength)
    t.lt(90)
    t.fd(96*sideLength)
    t.lt(90)
    t.fd((192*sideLength)/10)
    t.rt(135)
    t.fd((2592*sideLength)/100)
    t.left(135)
    t.fd(48*sideLength)
    t.lt(135)
    t.fd((2592*sideLength)/100)
    t.up()
    t.home()
    t.down()
    singleTab()

#Defining variable to use in while loop
shape2Draw=""

#Tab from turtle drawer to menu
singleTab()

#Loop process until "quit" is selected
while shape2Draw != 'Q':

#Menu options
    shape2Draw=input('''What would you like to draw?
(S)quare
(T)riangle
(R)ocket
(Q)uit\n''')
    shape2Draw=shape2Draw.upper()

#Drawing number of squares to specified sizes and locations
    if shape2Draw == "S":
        numOfObj=int(input("How many would you like to draw?\n"))       
        for x in range(0,numOfObj):
            startPosition()
            drawASquare()

#Drawing number of triangles to specified sizes and locations
    if shape2Draw == "T":
        numOfObj=int(input("How many would you like to draw?\n"))
        for x in range(0,numOfObj):
            startPosition()
            drawATriangle()

#Drawing number of rockets to specified sizes and locations
    if shape2Draw == "R":
        numOfObj=int(input("How many would you like to draw?\n"))
        for x in range(0,numOfObj):
            startPosition()
            drawARocket()

#quitting the loop
    if shape2Draw == "Q":
        print('''Thank you for choosing turtle drawing incorporated.
Have a nice day.''')

#Wrong choice
    if shape2Draw != "S" and shape2Draw != "T" and shape2Draw != "R" \
       and shape2Draw != "Q":
        print("I don't know how to draw that, please try again")
