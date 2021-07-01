#Starting map
classHrs={"class1":0,"class2":0,"class3":0}

#Asking for study hours per week (should)
class1Hrs=int(input("How many hours per week should you spend on your first class?\n"))
class2Hrs=int(input("How many hours per week should you spend on your second class?\n"))
class3Hrs=int(input("How many hours per week should you spend on your third class?\n"))

#Appending map with new hours
classHrs["class1"]=class1Hrs
classHrs["class2"]=class2Hrs
classHrs["class3"]=class3Hrs

#Asking for study hours per week (actual)
daysperWeek=int(input("\nHow many days per week will you study?\n"))
hrsperDay=int(input("How many hours per day do you currently study?\n"))

#comparing "should" hours to actual hours
shouldHrs=(class1Hrs+class2Hrs+class3Hrs)/daysperWeek
print('''\nYou currently study %d hours per day.
You should be studying %.1f hours per day.\n'''%(hrsperDay, shouldHrs))

#Response to comparison
if shouldHrs <= hrsperDay:
    print("You are probably studying enough.")
else:
    print("You should probably study more.")
