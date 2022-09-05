
###################################
# Arun - Python learning references.
# Log .
#####################################
name = "My first python code"
print(name)
upper_name = name.upper()
print(upper_name)
print('*' * 10)  ## This is quite good.
## get the value from user and process

## program to calcualte the age and print int the terminal
get_age = input("Enter your birth year: ")
cur_age = 2022 - int(get_age)
print(cur_age)

## String calculation
course = "Python for beginners"
print(course[0])
print(course[0:3]) ## for getting only first three characters

##working with strings
first = 'John'
last = 'smith'

print(first + '['+ last + ']' + 'is a coder')
msg = f'{first} [{last}]  is a coder' ## formated string - other option.
print(msg)

## String method

print(len(course)) ## length
print(course.find('P'))
print(course.replace('Python','python - '))   ## find and replace

print('Python' in course)  ## in operator

## operator precedence

x = 10 + 3 * 2
print(x)

x = 10 + (3*2)
print(x)

import math   ## will import maths as an object and can use . to access all mathamatical funcation available.

print(math.ceil(2.3))

## if Statements

is_hot = False
is_cold = False
if is_hot:
    print("hot day ")
    print("Drink plenty of water")
elif is_cold:
    print("its a cold day")
    print("remember to wear jacket")
else:
    print("its a lovely day")
print("Enjoy your day ")

## Logical operator and or  not

has_high_income = False
has_good_credit = True

if has_good_credit and has_high_income:
    print("eligible for credit")
else:
    print("Not eligible")

## comparison operator

temperature = 40

if temperature > 30:
    print("its a hot day")
else:
    print("Not a hot day")

###############################################\
# Start from 1:15 https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=40
##############################################
## while loops
i = 1
while i <= 5:
    print(i)
    i+=i
    if i==6:
        break
else:
    print("i am in else part")
    print("change the if statement and see how the code behaves")

print("done")


######################
#Car game
######################
c_quit = "QUIT"
c_count = 0
print
while 1 == 1:
    c_input = input(">")
    if c_input.upper() == "HELP":
        print("Start : for starting the car")
        print("Stop : for stop the car")
        print("quit : quit the car")
    elif c_input.upper() == "START":
        if c_count == 0:
            print("Car ready to go")
            c_count += 1
        else:
            print("car already started")
    elif c_input.upper() == "STOP":
        print("Car stopped")
    elif c_input.upper() == c_quit:
        break
else:
    print("done")

####################################
# For loops   start from 1:41 https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=41
#########################################

for item in 'pyton':
    print(item)

for list in ['Mosh','John','Arun']:
    print(list)

for num in [1,2,3,4]:
    print(num)
## for loop can be used to loop through a manually entered input too.
for a in get_age:
    print(a + "t")

for numrange in range(10):
    print(numrange)

print('*'*100)

for rumurange in range(5,15):
    print(rumurange)

print('*'*100)
for r_step_loop in range(1,10,2):  ##  skip 2,4,6  the last 2 parameter in range is the step.
    print(r_step_loop)

## for loop exersise

for price_list in [10,20,30]:
    psum = price_list + price_list
print(psum)

# Nested loop
print('*'*100)
for x_cod in range(3):
    for y_cod in range(3):
        print(f'{x_cod}, {y_cod}')
print("done")

f = [5,2,5,2,2]
for fval in f:
    print('X'*fval)
######################
#Lists
#####################
list_name = ['Aj','JA','aa']
print(list_name)
print(list_name[0]) ## first element of the list
print(list_name[0:3]) ## first three element of the list.
print(list_name[0].upper()) ## change the format of the string in the first element

list_largest = [10,53,454,67,33,674,10]
print(max(list_largest))

##########################
## 2D list
#########################

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0]) ## first row of the matrix
print(matrix[0][0]) ## the first element of the first row

## change the first element to 0
matrix[0][0] = 0
print(matrix[0][0]) ## changing the  first element of the first row
print('regenerate all the numbers of the matrix')
for mrow in matrix:
    for e in mrow:
        print(e)

print('done')

# add , remove, and append itmes to the list

list_name.append('JP')
print(list_name)
list_name.insert(0,'GR')
print(list_name)
## pop is for removing the last item in the list
## write a progrm to remove duplicate on the list
rem_dup = [10,53,454,67,67,33,674,10]
for i in rem_dup:
    dup = rem_dup.count(i)
    print(dup)
    if dup > 1:
        rem_dup.remove(i)
print(rem_dup)

#############################
#Tuples  - a list that you cannot change
#############################

my_fam = ('aj','aa','ja','jp','gr')
print(my_fam.count('aj'))

####################################
# Unpacking - start from 2:14 https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=42
####################################
# first lets take the same tuple created earlier or list
# assing all data to a variable
x=my_fam[0]
y=my_fam[1]
z=my_fam[2]
print(x,y,z)
## now unpacking
a,b,c,d,e = my_fam

print(a,b,d,e)
####################################
# Dictionaries - start from 2:18 https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=42
####################################
## Stores information in a key value pair
# Name:Arun
# email:arun.jayasundaran@gmail.com
#Phone: 0466099283
customer = {
    "name" : "Arun Jayasundaran",
    "age": 40,
    "email": "arun.jayasundaran@gmail.com"
}
## retriving the value from the key

print(customer["name"])

# adding a new component to the dictonary
customer["Address"]= "Unit 7 9 Drew Street, Parramatta, NSW 2150"

print(customer["Address"])
print(customer.get("name","not found"))


######################################
# Funcations  2:30 https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=43
######################################

def greet_user(p_fname,p_lname):
    print(f"Hi there {p_fname} " f" {p_lname}")
    print("Calling from a function")

print("start")
greet_user("Arun", "Jayasundaran")

greet_user(p_fname="Arun",p_lname="Jayasundaran")

print("end")


#  Funcations that return values  2:45 -- https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=43

def add_numbers(p_number, p_number1):
    return p_number +p_number1


val=add_numbers(1,1)
print(val)
print(add_numbers(3,4))

## exceptions
## The best way to find different exceptions are to type except and type the upper of one Char eg for Value error type V and wait

try:
    age=(int(input("Enter your age: >")))
except ValueError:
    print("Please dont enter char")

###################################
# Classes 3:01:58   https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=44
###################################

class point:
    def move(self):                 # this is called methods
        print("move")

    def draw(self):
        print("Draw")


v_point = point()
v_point.draw()
v_point.x = 10                      ## this is attributes
print(v_point.x)


## constructors

class xpoint:
    def __init__(self,x,y):          ## constructors -- remember it is init not int -- i had this issue earlier
        self.x=x
        self.y=y

    def move(self):                 # this is called methods
        print("move")

    def draw(self):
        print("Draw")



n_point=xpoint(10,20)
n_point.x

## exercise

class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Next talk {self.name} ")


v_person=Person("Arun")
v_person.talk()
#################################
#inheritance 3:14:55  https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=43
################################

class Mammal:
    def walk(self):
        print("walk")

class cat(Mammal):
    def cat(self):
        pass        ## python expect something inside a module, if you dont have anything, just say pass

class dog(Mammal):  ## Inherited from other class Mammal
    def dog(self):
        print("bark");

class human(Mammal):
    def brain(self):
        print("Human has intelligence ")

sweety = cat()
sweety.walk()
sweety.cat()

tommy=dog()
tommy.walk()
tommy.dog()

jack=human()
jack.brain()

#########################################
#Modules -- Creating a file and importing it in the main package. Lets create a file called cal_weight.py and import into this program 
###########################################
import CalWeight

v_w = input("Enter weight in Kg > ")
CalWeight.Cal_weight(v_w)

###############################
#packages  -- 3:30 https://www.youtube.com/watch?v=_uQrJ0TkZlc&list=PLR7Y-a2AjXWrtHCbYLPlBtIbBvZS8wVQa&index=44
# this can also sometimes refered as directories
# idea is to organised releated modules inside a package
# for this example, i am creatign an ecommerce package - the very basic one wich has just the print
##############################
import ecommerce.shipping

ecommerce.shipping.Cal_shipping_cost()

############################################################################################
# Standard libraries
# search in google -  python 3 modules indexe
# Below are some of the important ones.
#       date and time
#       sending emails
#       zip
#       deailing with excel
#       os and paths - all you need to do is to search and understand.
#############################################################################################


