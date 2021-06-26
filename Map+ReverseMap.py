import time
#Asking for first name
name1=input("Enter a name.\n")
name1=name1.rstrip()

#Asking for first number
number1=input("Enter their phone number.\n")
number1=number1.rstrip()

#Asking for second name
name2=input("Enter a name.\n")
name2=name2.rstrip()

#Asking for second number
number2=input("Enter their phone number.\n")
number2=number2.rstrip()

#Asking for third name
name3=input("Enter a name.\n")
name3=name3.rstrip()

#Asking for third number
number3=input("Enter their phone number.\n")
number3=number3.rstrip()

#put responses into map and show map
phoneBook={name1:number1,name2:number2,name3:number3}

#Asking for and finding a phone number by searching with a person
namSearch=input("\n\nWhich name would you like to find the phone number of?\n")
print("The phone number for %s is %s.\n\n"%(namSearch,phoneBook[namSearch]))
time.sleep(5)

#reversing "phone book" so keys become values and values become keys
reversedPhoneBook = dict(map(reversed, phoneBook.items()))

#Asking for and finding a person by searching with a phone number
numSearch=input("Which person would you like to find via phone number?\n")
print("The person with the phone number %s is %s.\n"%(numSearch,reversedPhoneBook[numSearch]))
