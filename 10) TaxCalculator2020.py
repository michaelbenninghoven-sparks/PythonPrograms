#Putting tax brackets into variables
sMax10=int(9875)
sMax12=int(40125)
sMax22=int(85525)
sMax24=int(163300)
sMax32=int(207350)
sMax35=int(518400)
mfjMax10=int(19750)
mfjMax12=int(80250)
mfjMax22=int(171050)
mfjMax24=int(326600)
mfjMax32=int(414700)
mfjMax35=int(622050)
mfsMax35=int(311025)
hohMax10=int(14100)
hohMax12=int(53700)
hohMax22=int(85500)
hohMax24=int(163300)
hohMax32=int(207350)
hohMax35=int(518400)

#Tax calculations single
sBracket1=((sMax10-0)*.1)
sBracket2=sBracket1+((sMax12-sMax10)*.12)
sBracket3=sBracket2+((sMax22-sMax12)*.22)
sBracket4=sBracket3+((sMax24-sMax22)*.24)
sBracket5=sBracket4+((sMax32-sMax24)*.32)
sBracket6=sBracket5+((sMax35-sMax32)*.35)

#Tax calculations Married filing Jointly
mfjBracket1=((mfjMax10-0)*.1)
mfjBracket2=mfjBracket1+((mfjMax12-mfjMax10)*.12)
mfjBracket3=mfjBracket2+((mfjMax22-mfjMax12)*.22)
mfjBracket4=mfjBracket3+((mfjMax24-mfjMax22)*.24)
mfjBracket5=mfjBracket4+((mfjMax32-mfjMax24)*.32)
mfjBracket6=mfjBracket5+((mfjMax35-mfjMax32)*.35)

#Tax calculations Married filing Seperately
mfsBracket1=((sMax10-0)*.1)
mfsBracket2=sBracket1+((sMax12-sMax10)*.12)
mfsBracket3=sBracket2+((sMax22-sMax12)*.22)
mfsBracket4=sBracket3+((sMax24-sMax22)*.24)
mfsBracket5=sBracket4+((sMax32-sMax24)*.32)
mfsBracket6=sBracket5+((mfsMax35-sMax32)*.35)

#Tax calculations Head of Houshold
hohBracket1=((hohMax10-0)*.1)
hohBracket2=hohBracket1+((hohMax12-hohMax10)*.12)
hohBracket3=hohBracket2+((hohMax22-hohMax12)*.22)
hohBracket4=hohBracket3+((hohMax24-hohMax22)*.24)
hohBracket5=hohBracket4+((hohMax32-hohMax24)*.32)
hohBracket6=hohBracket5+((hohMax35-hohMax32)*.35)

#Asking for filing status
print("This program will tell you how much you paid to taxes in 2020.\n")
filingStatus=input('''What is your filing status?\n
s = single
mfj = married filing jointly
mfs = married filing seperately
hoh = head of household\n\n''')

#SINGLE
if filingStatus == "single" or filingStatus == "s":
    print("You chose single\n")
    taxableIncome=int(input("What was your taxable income (after deductions and exemptions) this year?\n"))

#single 10% bracket
    if taxableIncome <= sMax10:
        Tax=(taxableIncome-0)*.1
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 10 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#single 12% bracket
    if taxableIncome > sMax10 and taxableIncome <= sMax12:
        Tax=sBracket1+((taxableIncome-sMax10)*.12)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 12 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#single 22% bracket
    if taxableIncome > sMax12 and taxableIncome <= sMax22:
        Tax=sBracket2+((taxableIncome-sMax12)*.22)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 22 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#single 24% bracket
    if taxableIncome > sMax22 and taxableIncome <= sMax24:
        Tax=sBracket3+((taxableIncome-sMax22)*.24)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 24 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#single 32% bracket
    if taxableIncome > sMax24 and taxableIncome <= sMax32:
        Tax=sBracket4+((taxableIncome-sMax24)*.32)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 32 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#single 35% bracket
    if taxableIncome > sMax32 and taxableIncome <= sMax35:
        Tax=sBracket5+((taxableIncome-sMax32)*.35)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 35 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#single 37% bracket
    if taxableIncome > sMax35:
        Tax=sBracket6+((taxableIncome-sMax35)*.37)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 37 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#MARRIED FILING JOINTLY

if filingStatus == "married filing jointly" or filingStatus == "mfj":
    print("You chose married filing jointly\n")
    taxableIncome=int(input("What was your taxable income (after deductions and exemptions) this year?\n"))

#married filing jointly 10% bracket
    if taxableIncome <= mfjMax10:
        Tax=(taxableIncome-0)*.1
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 10 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing jointly 12% bracket
    if taxableIncome > mfjMax10 and taxableIncome <= mfjMax12:
        Tax=mfjBracket1+((taxableIncome-mfjMax10)*.12)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 12 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing jointly 22% bracket
    if taxableIncome > mfjMax12 and taxableIncome <= mfjMax22:
        Tax=mfjBracket2+((taxableIncome-mfjMax12)*.22)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 22 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing jointly 24% bracket
    if taxableIncome > mfjMax22 and taxableIncome <= mfjMax24:
        Tax=mfjBracket3+((taxableIncome-mfjMax22)*.24)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 24 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing jointly 32% bracket
    if taxableIncome > mfjMax24 and taxableIncome <= mfjMax32:
        Tax=mfjBracket4+((taxableIncome-mfjMax24)*.32)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 32 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing jointly 35% bracket
    if taxableIncome > mfjMax32 and taxableIncome <= mfjMax35:
        Tax=mfjBracket5+((taxableIncome-mfjMax32)*.35)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 35 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing jointly 37% bracket
    if taxableIncome > mfjMax35:
        Tax=mfjBracket6+((taxableIncome-mfjMax35)*.37)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 37 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#MARRIED FILING SEPERATELY

if filingStatus == "married filing seperately" or filingStatus == "mfs":
    print("You chose married filing seperately\n")
    taxableIncome=int(input("What was your taxable income (after deductions and exemptions) this year?\n"))

#married filing seperately 10% bracket
    if taxableIncome <= hohMax10:
        Tax=(taxableIncome-0)*.1
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 10 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing seperately 12% bracket
    if taxableIncome > sMax10 and taxableIncome <= sMax12:
        Tax=mfsBracket1+((taxableIncome-sMax10)*.12)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 12 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing seperately 22% bracket
    if taxableIncome > sMax12 and taxableIncome <= sMax22:
        Tax=mfsBracket2+((taxableIncome-sMax12)*.22)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 22 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing seperately 24% bracket
    if taxableIncome > sMax22 and taxableIncome <= sMax24:
        Tax=mfsBracket3+((taxableIncome-sMax22)*.24)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 24 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing seperately 32% bracket
    if taxableIncome > sMax24 and taxableIncome <= sMax32:
        Tax=mfsBracket4+((taxableIncome-sMax24)*.32)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 32 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing seperately 35% bracket
    if taxableIncome > sMax32 and taxableIncome <= mfsMax35:
        Tax=mfsBracket5+((taxableIncome-sMax32)*.35)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 35 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#married filing seperately 37% bracket
    if taxableIncome > mfsMax35:
        Tax=mfsBracket6+((taxableIncome-mfsMax35)*.37)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 37 percent bracket.
You have been taxed %d dollars this year.
This was %d percent of your total earnings this year'''%(Tax, taxPercent))

#HEAD OF HOUSEHOLD

if filingStatus == "head of household" or filingStatus == "hoh":
    print("You chose head of household\n")
    taxableIncome=int(input("What was your taxable income (after deductions and exemptions) this year?\n"))

#head of household 10% bracket
    if taxableIncome <= hohMax10:
        Tax=(taxableIncome-0)*.1
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 10 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#head of household 12% bracket
    if taxableIncome > hohMax10 and taxableIncome <= hohMax12:
        Tax=hohBracket1+((taxableIncome-hohMax10)*.12)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 12 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#head of household 22% bracket
    if taxableIncome > hohMax12 and taxableIncome <= hohMax22:
        Tax=hohBracket2+((taxableIncome-hohMax12)*.22)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 22 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#head of household 24% bracket
    if taxableIncome >= hohMax22 and taxableIncome <= hohMax24:
        Tax=hohBracket3+((taxableIncome-hohMax22)*.24)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 24 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#head of household 32% bracket
    if taxableIncome > hohMax24 and taxableIncome <= hohMax32:
        Tax=hohBracket4+((taxableIncome-hohMax24)*.32)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 32 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#head of household 35% bracket
    if taxableIncome > hohMax32 and taxableIncome <= hohMax35:
        Tax=hohBracket5+((taxableIncome-hohMax32)*.35)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 35 percent bracket.
You have been taxed %d dollars this year.
This was roughly %d percent of your total earnings this year'''%(Tax, taxPercent))

#head of household 37% bracket
    if taxableIncome > hohMax35:
        Tax=hohBracket6+((taxableIncome-hohMax35)*.37)
        taxPercent=(Tax/taxableIncome*100)
        print('''\nYou fall into the 37 percent bracket.
You have been taxed %d dollars this year.
This was %d percent of your total earnings this year'''%(Tax, taxPercent))



#WRONG CHOICE
if filingStatus != "single" and \
filingStatus != "married filing jointly" and \
filingStatus != "married filing seperately" and \
filingStatus != "head of household" and \
filingStatus != "s" and \
filingStatus != "mfj" and \
filingStatus != "mfs" and \
filingStatus != "hoh":
    print('''I\'m not aware of this filing status.
Please try again.''')
