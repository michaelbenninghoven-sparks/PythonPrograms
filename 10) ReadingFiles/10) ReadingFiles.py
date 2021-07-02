##import libraries##
import csv
import turtle as t

##Reading the csv file##
print("Reading file into list...")
with open("C:\School\IT 121 Intro to Programming\Final/stockIndex.csv","r") as csvfile:
    csvreader=csv.reader(csvfile)

##Displaying the data##
    print("The data in the list...")
    stockPts=[]
    stockPts2=[]
    for row in csvreader:
        stockPts.append(row)
    print(stockPts)
    
##Drawing the graph##
    print("Drawing the graph...")

    ##Setting start point##
    t.up()
    t.goto(-160,0)
    t.down()

    ##Y-Axis Lines##
    def axisLine():
        t.lt(90)
        t.fd(10)
        t.lt(90)
        t.fd(5)
        t.lt(180)
        t.fd(10)
        t.bk(5)
    for x in range(0,20):
        axisLine()

    ##Y-Axis Scale##
    t.up()
    t.bk(30)
    t.rt(90)
    t.fd(7)
    yNum=200
    for x in range(0,10):
        t.write(yNum)
        t.fd(20)
        yNum-=20

    ##Y-Axis Label##
    t.goto(-280,93)
    t.write("Stock Index")

    ##X-Axis Lines##
    t.goto(-160,0)
    t.down()
    for x in range(0,30):
        axisLine()

    ##X-Axis Scale##
    t.up()
    t.fd(20)
    t.rt(90)
    t.fd(4)
    xNum=30
    for x in range(0,6):
        t.write(xNum)
        t.fd(50)
        xNum-=5

    ##X-Axis Label##
    t.goto(-20,-40)
    t.write("days")

##Drawing the data##
    print("Drawing the data...")

    ##Setting Start Point##
    t.up()
    t.goto(-150,100)
    t.down()
    t.width(2)

    ##Drawing graph line##
    for row in stockPts:
        stockPts2.append(row[1])
        for x in range(0,len(stockPts2)):
            stockPts2[x] = int(stockPts2[x])
        for x, y in zip(stockPts2, stockPts2[1:]):
            if x > y:
                t.color("red")
            else:
                t.color("green")
        x=float(row[0])
        y=float(row[1])
        t.goto((x-16)*10,y)
