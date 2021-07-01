#Extra components needed to transition to drawing environment.
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

#Create drawing environment
    import turtle
    t=turtle.Pen()

#Changing to turtle drawing window
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt

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





#DIAMOND
if shape2Draw == "diamond":
    sideLength=int(input("How long, in pixles, would you like the sides to be?\n"))

#Create drawing environment
    import turtle
    t=turtle.Pen()

#Changing to turtle drawing window
    user32.keybd_event(0x12, 0, 0, 0) #Alt
    sleep(1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)
    user32.keybd_event(0x09, 0, 0, 0) #Tab
    sleep(0.1)
    user32.keybd_event(0x09, 0, 2, 0) #~Tab
    sleep(0.1)
    user32.keybd_event(0x12, 0, 2, 0) #~Alt

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




#RECTANGLE
if shape2Draw == "rectangle":
    sideLength=int(input("How long, in pixels, would you like this rectangle?\n"))
    sideWidth=int(input("How wide, in pixels, would you like this rectangle?\n"))

#Statement for choosing rectangle and making a square.
    if sideLength == sideWidth:
        print('''You should have picked a square,
but this is still technically a rectangle, so here you go.''')
        sleep(5)

#Create drawing environment
        import turtle
        t=turtle.Pen()

#Changing to drawing environment window.
        user32.keybd_event(0x12, 0, 0, 0) #Alt
        sleep(1)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
        user32.keybd_event(0x09, 0, 2, 0) #~Tab
        sleep(0.1)
        user32.keybd_event(0x12, 0, 2, 0) #~Alt
        
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

    else:

#Create drawing environment
        import turtle
        t=turtle.Pen()

#Changing to drawing environment window.
        user32.keybd_event(0x12, 0, 0, 0) #Alt
        sleep(1)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
        user32.keybd_event(0x09, 0, 0, 0) #Tab
        sleep(0.1)
        user32.keybd_event(0x09, 0, 2, 0) #~Tab
        sleep(0.1)
        user32.keybd_event(0x12, 0, 2, 0) #~Alt
        
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
