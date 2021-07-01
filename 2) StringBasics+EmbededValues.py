import time

#Using single quotes
print('This is what a print statement looks like with single quotes.\n')
time.sleep(3)

#Using double quotes
print("I see no difference with double quotes.\n")
time.sleep(3)

#Using triple quotes and '\' for an apostrophe
print('''Now you\'re asking me to use triple quotes.
This allows for multiple lines.\n''')
time.sleep(3)

#Using %s, %d, and %f
clas="Intro to Programming"
teacher="Mike Massey"
integer=50
num=99.999
print('''I\'m having so much fun in %s with %s.
There\'s not just a %d percent chance, '''%(clas, teacher, integer),end="")
print('''but a %.3f percent chance I\'ll finish
most of the labs early.\n''' %(num))
time.sleep(10)

#multiplying strings and ending newline of a print statement.
print("bad horse \n"*4,end="")
print('''he rides across the nation
the thoroughbred of sin
he got the application
that you just sent in
it needs evaluation
so let the games begin
a heinous crime
a show of force
a murder would be nice of course''')
print("bad horse \n"*3,end="")
print('''the evil league of evil
is watching so beware
the grade that you receive
will be your least we swear
so make the bad horse gleeful
or he\'ll make you his mare
you\'re saddled up
there\'s no recourse
it\'s hi-ho silver
signed bad horse.''')
