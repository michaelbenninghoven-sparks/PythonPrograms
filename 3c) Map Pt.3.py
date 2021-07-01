#Starting map and list
classHrs={}
hrsList=[]

#Asking for number of classes
numClass=int(input("How many classes do you have?\n"))

#Asking for study hours per week (should)
for x in range (1,numClass+1):
    classxHrs=int(input("How many hours per week should you spend on class %s?\n"%x))
    
#Appending map with new hours
    classHrs["class %s"%x]=classxHrs

#Asking for study hours per week (actual)
daysperWeek=int(input("\nHow many days per week do you study?\n"))
hrsperDay=int(input("\nHow many hours per day do you currently study?\n"))

#taking values from map and placing in list.
while numClass > 0:
    hrsList.append(classHrs["class %s"%numClass])
    numClass=numClass-1

#comparing "should" hours to actual hours
shouldHrs=(sum(hrsList))/daysperWeek

print('''\nYou currently study %d hours per day.
You should be studying %.1f hours per day.\n'''%(hrsperDay, shouldHrs))

#Response to comparison
if shouldHrs <= hrsperDay:
    print("You are probably studying enough.")
else:
    print("You should probably study more.")
