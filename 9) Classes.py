class Employee:

#Common base class for all employees
    empCount=0
    def __init__(self,firstName,lastName,salary):
        self.firstName=firstName
        self.lastName=lastName
        self.salary=salary
        Employee.empCount += 1
        self.empNum = Employee.empCount

    def displayCount(self):
        print("%s %s is employee %d of %d"%(self.firstName,self.lastName, \
                                            self.empNum,Employee.empCount))

    def displayEmployee(self):
        print("Name:",self.firstName,self.lastName,"Salary:",self.salary)

#These would create two objects of class Employee 
Luke=Employee("Luke","Skywalker",2000)
Han=Employee("Han","Solo",3000)

print("After adding Luke Skywalker and Han Solo to employee class.\n")

#Using functions of Employee class
Employee.displayEmployee(Luke)
Employee.displayCount(Luke)
Employee.displayEmployee(Han)
Employee.displayCount(Han)

#Manager class derived from Employee that also has a department and can adjust salaries
class Manager(Employee):
    def __init__(self,firstName,lastName,salary,department):
        self.department=department
        Employee.__init__(self,firstName,lastName,salary)

    def displayManager(self):
        self.displayEmployee()
        print("%s %s manages the %s department."%(self.firstName,self.lastName,self.department))

    def adjustSalary(self,employee,amount,reason):
        employee.salary += amount
        print("%s %s\'s new salary is %s."%(employee.firstName,employee.lastName, \
                                            employee.salary))
        print("Reason for adjustment: %s"%reason)

    def forceChoke(self,employee,reason):
        print("%s %s has been force choked."%(employee.firstName,employee.lastName))
        print("Reason for strangulation: %s"%reason)
              
#Create a new instance of a Manager which also includes all the attributes of an Employee
Vader=Manager("Darth","Vader",4500,"Death Star")

print('''\nAfter adding Darth Vader to Manager class
which was derived from Employee class''')

#Using functions of Employee class with managers
print("Using Employee functions on member of Manager class.\n")
Vader.displayCount()
Vader.displayEmployee()

#Using functions of Manager class
print("\nUsing Manager class functions.\n")
Vader.displayManager()
Vader.adjustSalary(Han,-50,"Being lazy")
Vader.forceChoke(Luke,"Joined the rebellion")

#stormtrooper class derived from Employee
class Stormtrooper(Employee):
    def __init__(self,firstName,lastName,salary,position):
        self.position=position
        Employee.__init__(self,firstName,lastName,salary)
        
    def displayTrooper(self):
        self.displayEmployee()
        print("Trooper %s is a %s and makes %d."\
              %(self.lastName,self.position,self.salary))

    def fireShot(self):
        shotFired=input("Who are you trying to fire at?\n")
        shotFired=shotFired.upper()
        if shotFired == "DARTH" or shotFired == "VADER" \
           or shotFired == "DARTH VADER":
            print("You finally hit something.")
            Vader.forceChoke(newTrooper,"You shot Darth Vader!")
        else:
            print("You're a stormtrooper. You cant hit anything.")
            Vader.adjustSalary(newTrooper,-20,"You missed!")
        
print("\nAfter adding Stormtrooper class derived from employee class\n")

#Storm trooper info
trooperFirst=input("What is the stormtrooper's first name?\n")
trooperLast=input("What is the stormtrooper's last name?\n")
trooperWage=int(input("How much does this stormtrooper make?\n"))
trooperPosition=input("What kind of weapon specialist is this stormtrooper?\n")

#New member of Stormtrooper class
newTrooper=Stormtrooper(trooperFirst,trooperLast,trooperWage,trooperPosition)

#Using Employee class functions on member of Stormtrooper class
print("\nUsing functions of Employee class with member of Stormtrooper class.\n")
newTrooper.displayEmployee()
newTrooper.displayCount()

#Using Stormtrooper class functions
print("\nUsing functions of Stormtrooper class.\n")
newTrooper.displayTrooper()
newTrooper.fireShot()

        
