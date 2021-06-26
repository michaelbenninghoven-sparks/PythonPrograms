#Extra libraries needed to transition to drawing environment.
from time import sleep
import ctypes
user32 = ctypes.windll.user32

#Prompt user for shape input
shape2Draw=input("Would you like to draw a square, diamond, or rectangle?\n")

#wrong choice
if shape2Draw != "square" and shape2Draw != "rectangle" and shape2Draw != "diamond":
    print('''This shape does not exist in my database.
Please try again next time.\n''')
    
#SQUARE
if shape2Draw == "square":

#Ask for length of square sides
    sideLength=int(input("How long, in pixles, would you like the sides to be?\n"))
    OpenWindows=int(input("How many windows do you currently have open?\n"))

#Create drawing environment
    import turtle
    t=turtle.Pen()

#Changing to turtle drawing window
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(1)
    for x in range(0,OpenWindows):
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt

#while loop
while shape2Draw == "square":

#Drawing square to requested size
    t.up()
    t.forward(sideLength/2)
    t.left(90)
    t.forward(sideLength/2)
    t.left(180)
    t.down()
    t.forward(sideLength)
    t.right(90)
    t.forward(sideLength)
    t.right(90)
    t.forward(sideLength)
    t.right(90)
    t.forward(sideLength)
    t.up()
    t.right(90)
    t.forward(sideLength/2)
    t.right(90)
    t.forward(sideLength/2)
    t.down()
    sideLength=sideLength+5




#DIAMOND
if shape2Draw == "diamond":
    sideLength=int(input("How long, in pixles, would you like the sides to be?\n"))

#Create drawing environment
    import turtle
    t=turtle.Pen()

#Changing to turtle drawing window
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(1)
    for x in range(0,OpenWindows):
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt

#while loop
while shape2Draw == "diamond":

#Drawing diamond to requested size
    t.up()
    t.forward(sideLength/2)
    t.left(135)
    t.down()
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.left(90)
    t.forward(sideLength)
    t.up()
    t.left(135)
    t.forward(sideLength/2)
    t.left(180)
    t.down()
    sideLength=sideLength+5



#RECTANGLE
if shape2Draw == "rectangle":
    sideLength=int(input("How long, in pixels, would you like this rectangle?\n"))
    sideWidth=int(input("How wide, in pixels, would you like this rectangle?\n"))

#Create drawing environment
    import turtle
    t=turtle.Pen()

#Changing to drawing environment window.
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(1)
    for x in range(0,OpenWindows):
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt

#while loop
while shape2Draw == "rectangle":
    
#Drawing the requested rectangle
    t.up()
    t.forward(sideLength/2)
    t.down()
    t.right(90)
    t.forward(sideWidth/2)
    t.right(90)
    t.forward(sideLength)
    t.right(90)
    t.forward(sideWidth)
    t.right(90)
    t.forward(sideLength)
    t.right(90)
    t.forward(sideWidth/2)
    t.up()
    t.right(90)
    t.forward(sideLength/2)
    t.down()
    sideLength=sideLength+5
    sideWidth=sideWidth+5
