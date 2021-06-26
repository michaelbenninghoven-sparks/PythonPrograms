#Create drawing environment
import turtle
t=turtle.Pen()

#Load random tools library
import random

#Moving turtle in endless dash line loop
while True:
    t.fd(5)

#Displaying (x,y) positions and heading
    x,y=t.position()
    z=t.heading()
    print(x,y,z)

#Change heading left if at right edge
    if x >= 200:
        z=random.randint(100,260)
        t.setheading(z)

#Change heading down to the right if at left edge in top half 
    elif x <= -200 and y >= 0:
        z=random.randint(280,350)
        t.setheading(z)

#Change heading up to the right if at left edge in bottom half
    elif x <= -200 and y < 0:
        z=random.randint(0,80)
        t.setheading(z)

#Change heading down if at top edge
    elif y >= 200:
        z=random.randint(190,350)
        t.setheading(z)

#Change heading up if at bottom edge
    elif y <= -200:
        z=random.randint(10,170)
        t.setheading(z)

