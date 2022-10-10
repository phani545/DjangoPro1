#WelCome Phani

from datetime import date
import random
import sys
from functools import reduce
"""
print("Hello Phani");

#caluclate the numbers

a,b,c,d = 100,200,300,400
sum = a+b+c+d
print("Sum of values", sum)

#to know type of vaviable

print(type(a))



#Caluclate the sum of variables 
sum = 10
def caluclate():
    currentSum = 100
    totalSum = sum + currentSum
    print(totalSum)

caluclate();
#O/P: 110
#print("currentSum", currentSum) => Given error which ias not defined in scope


sum = 10
def caluclate():
    sum = 30 #when we assign value to sum variable then its become the new variable in function.   
    sum = sum + 20
    currentSum = 200
    totalSum = sum + currentSum
    print("Inner Scope:",totalSum)

caluclate();
print("Outer Scope:",sum)
O/p:

250
10

sum = 10
def caluclate():
    global sum #If we define a global keyword to sum variable then perform like global varible.    
    sum = sum + 20
    currentSum = 200
    totalSum = sum + currentSum
    print("Inner Scope:",totalSum)

caluclate();

print("Outer Scope:",sum)
O/P:
230
30

==============================================
##Program to demonistrate the Input && output
==============================================
cash = 1000
remainingAmount = 40000
print("Take your cash::",cash,remainingAmount,sep = " ===> ",end = "\t")#seperator gives spaces between the output.; Default end value is \n; 
print("ThankYou!!!",end = "===")
print("ThankYou!!!")

=======================
 Interview Questions::
=======================
1)How to print without new line? Print values using end keyword just replace default value \n with  'spaces(")' or '\t' ex: end = "\t" end =" ## ".


## program with input keyword.
cash = int(input("Enter your cash::")) #Convert one type to other type is called typecasting.Bydefault entered valued through input are stings.
print("TYPE OF CASH IS ::", type(cash))
atmAmount = 50000
remainingAmount = 50000 - cash
print("Take your cash & remainingAmount::",cash,remainingAmount,sep = " ===> ",end = "\t")#seperator gives spaces between the output.; Default end value is \n; 
print("ThankYou!!!",end = "===")
print("ThankYou!!!")


## program with multiples input.
pin,cash = input("Enter your pin and cash::").split(",") 
cashValue = int(cash)
print("PIN IS:", pin)
#Convert one type to other type is called typecasting.Bydefault entered valued through input are stings.
#print("TYPE OF CASH IS ::", type(cash))
atmAmount = 50000
remainingAmount = 50000 - cashValue
print("Take your cash & remainingAmount::",cashValue,remainingAmount,sep = " ===> ",end = "\t")#seperator gives spaces between the output.; Default end value is \n; 
print("ThankYou!!!",end = "===")
print("ThankYou!!!")



#Operator - used to perform various operations on values and variables.

a=int(input(print("Enter the value for a::")))
b=int(input(print("Enter the value for b::")))
c=a+b # operator Addition (+) perform the addition operation between the two operands.
print("Values for a => b => c ::", a,b,c , sep = " => ")


Different Operators
======================
-Arithmetic
-Relational Operators(Comparison)
-Assignment
-Logical
-Bitwise






## program with multiples input output formates.
pin,cash = input("Enter your pin and cash::").split(",") 
cashValue = int(cash)
print("PIN IS:", pin)
#Convert one type to other type is called typecasting.Bydefault entered valued through input are stings.
#print("TYPE OF CASH IS ::", type(cash))
atmAmount = 50000
remainingAmount = 50000 - cashValue
#print("Take your cash & remainingAmount::",cashValue,remainingAmount,sep = " ===> ",end = "\t")#seperator gives spaces between the output.; Default end value is \n; 
print("Take your cash {} and balance amount {}" .format(cashValue,remainingAmount),sep="==>") #formate methode
print("Take your cash {1} and balance amount {0}" .format(cashValue,remainingAmount),sep="==>") #formate methode with place holders
print("ThankYou!!!",end = "\n")
print("ThankYou!!!")




#Operators Program
#Arithmetic
print("Operator Programs::")

print("Arithmetic Programs::")
a=300
b=80
print("Addition", a+b)
print("Subtraction",a-b)
print("Multiplication",a*b)
print("division with float", a/b)
print("division with flooring",a//b)
print("Modular",a%b)
print("Returns first to the power of second",a**b)



#Relational Operators(Comparison)

print("Relational Operators::")

a=9
b=2

print(a==b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a!=b)


#Logical  ==> AND OR NOT

a= True
b= False

print(a and b)#False
print(a or b)#True
print(not a)#False
print(not b)#True


##Caluclate the age of person
YOB = int(input(print("Enter your Birth of year:")))
currentYear = date.today().year
Age= currentYear - YOB
print("Age is: {}" .format(Age)) 


Build In data types in python:
==============================

Mutable   - Can be replaced or altered
Immutable - Can't be replaced or altered.
Hashable  - Any Immutable object called as hasable. 

In python, every datatypes are classes and varibles are instance. here, no need to create the object by default it will create.

*Numeric(Int :- 1,2,3 float :- 12.234,Complex :- 10i + 2j )
*Sequence Types(strings - Immutable,list,tuple)
*Boolean
*Set
*Dictionary


print("DATA TYPES!!!")
#Numeric(Int :- 1,2,3 float :- 12.234,Complex :- 10i + 2j )

marks = 509
percentage = (marks/600)*100
print("Percentage of marks: {}" .format(percentage))
print (type(marks))
print (type(percentage))

com = 10 + 12j
c1  = 12 + 3j
print(type(com))
print(com.real)
print(com.imag)

print(com.conjugate())
print(com+c1)

##Cmath  - Advance cource for complex number. cmath one type of library


#String

#indexing 
chaneelName = "PhaniDeep"##based on the strings values we need to choose single quotes('') or double quotes("")
c='PhaniDeep'
c2='''Phani'''#for multiline strings
print(chaneelName)
print(c)
print(c2)

cn=len(chaneelName)
print(c[1],c[-1],sep = "===> ")
 



#Slicing

c='PhaniDeep'
c2='''Phani'''#for multiline strings
print(c)
print(c[1:3])
print(c[1:10:2])
print(c[:10])
print(c[:])
print(c[::2])
print(c[::-1])

#del c - delete strings

#Concatenation  - Joining strings two or more strinfs are called concatenation.

c3 = "Phani" + "Deep"
c4 = "Phani" + "Deep" *3

print(c3)
print(c4)

#string membership operators- IN OR NOT IN
print("Phani" in c4)
print("Boina" not in c4)
"""
"""

===============================================================================================================================
List - holds heterogenous data (differrent types of data).Ordered collection of items, these are mutable.Allow duplicate values.
     -  lisi wo members called empty list. a = b[];
     -  We can keep one list in other list called nested list.
================================================================================================================================     
     

print("============LISTS===============")
marks = [91,98,97,96,82,"phani",98] 
print(type(marks))
print(marks)
friends = ["Nandhu","Venkat","Giri","Raj"]
print("friends count", len(friends))
print(friends)
a = []
bioData = ['33',"9999234","address",friends]
print(bioData)
#Accessing elements - by using Indexing, will specipy index in +ve OR -ve values.
print("SecondFriends", friends[1])
print("LastFriends", friends[-1])
#Accessing elements from listedList
print(bioData[3][2])

marks[1] = 54

print(marks + friends )
print(friends*2)

#Adding elements to list - To add single item append(); More than one element - extend();
friends.append("robin")
print(friends)
friends.extend(["Raju","Ravi"])
print(friends)

#To Add element intp specific position - insert(position,value); insert multiple values at specific position using slicing;

friends.insert(1,"RaviKumar")#inert element at specific position
print(friends)

friends[1:1]=["aa","bbb","ccc","ddd"]#insert multiple elements at specified locations
print(friends)

del friends[1]#delete element at specific elements
print(friends)

del friends[1:3]#delete slicing/range of elements in list

print(friends)

#del friends#delete friend list

#print(friends)

#remove particle item

friends.remove("Raju")
print(friends)

#pop - remove and return speecified element, remove   element from last.
print(friends.pop(0))
print(friends.pop())
print(friends.clear())

############################################################################
Tuple  - ordercollection & immutable(can't remove element), store heterogenious data
         allow duplicate date like list
         use () paranthesis to create tuple
         we can't delete elements because its immutable
         but delete entire tuple
#############################################################################

markst = (20,50,30,40)
print(type(markst))
print(markst)
friends = ("Nandhu","Venkat","Giri","Raj",20,[12,32,545])
print(friends)

#Nexted tuple
biodata = ('33',"9999234","address",friends)
print(biodata)
print(biodata[3][1])

#Create tuple without paranthesis
biodata1 = '33',"9999234","address",friends
print(type(biodata1))
print(biodata1)

#If tuple have only element, its automatically convert as string.
a1 = ("HYD")
print(type(a1))
print(a1)
a1 = ("HYD",)#Need to put comma(,) we make it as tuple.
print(type(a1))
print(a1)

##Accessing elements

print(friends[0])
#print(friends[10]) get index error out of range
print(friends[-1])
#print(friends[-1.90])#Type error
friends[5][1]="sadf"
print(friends)
#to convert tuple to list
f1=list(friends)
print(type(f1))



##########################################################################
Boolean  == > these are used to assign & compare the values
              if value is 0 return the false 

###########################################################################



print("######Boolean############")
subcribed = True
print(type(subcribed))

a = 100

b = 100

print(type(a==b))

print(bool(a))#



##############################################################################################################

Set  - unodered collection of items. 
       Mutable(replace items) & not allow duplicate items.
       to identify particular element performance of set very good.
       {}
       set() - builtin funtion
       we can perform differrent operations in set like union, intersection, difference & symmetric_difference.
       we can use either operators or methods
       
FrozenSets - Immutable versions of set.       
###############################################################################################################


print("#######SET#########")
anchours = {"udhaya","suma","sudheer","ravi"}
print(type(anchours))
#Empty set empltyset = {} ===> becomes dictonary
emptyset = set()
print(type(emptyset))

#Indexing ==> indexing or scliling not using in sets because its unordered data.
anchours.add("Phani")#add to use add one new element. 
print(anchours)
anchours.update(["Deep","Challa"])## addping multiple elements to set by using update
print(anchours)
#remove the elements
anchours.discard("ravi")
print(anchours)
anchours.remove("suma")
print(anchours)
#difference between the discard & remove::If we specified element is not present in discard its not give error but remove will give the error.
anchours.discard("ravi")##===>Not Gives the error.
print(anchours)
#anchours.remove("suma")===>Gives the error.
print(anchours)
anchours.clear()##clear all elements.
print(anchours)
print("UNION")
a= {12,33,43,56,55}
b={21,34,54,33,53}
abunion =  a.union(b) #a | b set of all elements from both sets.
print(abunion)
abintersection = a.intersection(b)#a & b comman elements
print(abintersection)
abdefference = a.difference(b) # a - b set of elements which only in A not in BaseException
print(abdefference)
absymmetric_difference = a.symmetric_difference(b)#a^b :: set of elements which are present in A & B but not in both. 
print(absymmetric_difference)
##########################################################################
Dictionary - unordered collection of items; 
             mutable(can change)
             we can search the meaning word based on character(this character will act as key here) 
             Its holds key & value
             syntax :: friends = {key:value, key:value}
             Values -- can be duplicated where as keys can't be duplicated
             keys must be unique & immutable
             we can also use dict() to create a dictionary.             
#########################################################################


print("Dictionary")
bioData = {"name":"Phani","Add":"Choragusi"}
print(type(bioData))
print(bioData)
info = {"Channel":"Phanitech","info":bioData}#nested Different
print(info)

print(info["Channel"])##[] ==> key error will raise if the key is not found
print(info.get("Channel"))##get() ===> returns None if the key is not found

D1 = {1:{'Class' : 'B.Tech CSE', 'percentage' : 78.50},
      2:{'Class' : 'B.Tech CSE', 'percentage' : 70.50},
      3:{'Class' : 'B.Tech CSE', 'percentage' : 73.50}}

print(D1)
rollNumber = int(input("Enter your rollNumber:"))
percentage = D1[rollNumber]['percentage']
print("percentage is {}:" .format(percentage))
if(percentage > 40):
    print("PASSED")
else:
    print("FAILED")

##Accessing elements
info["Channel"] = "Phani Great Person"#Modified values
print(info)

info["Followed"] = True;##if key value is not present its add to dictionary otherwise its modifies.
print(info)
del info["Channel"]

print(info)#Delete elemet if not existing throws error.
#Pop
#Clear

#######################################################################################################
ControlFlow :: its very important to build complex programs.
               If  Condition:  
                    statemets;

               
#######################################################################################################


print("####ControlFlow####")
lastBall = 4
if (lastBall == 6):
    print("WON")
else:
    print("LOSE")
    
####check number is even or odd

num = int(input("ENTER THE NUMBER:"))
if(num%2 == 0):
    print("{} NUMBER IS EVEN" .format(num))
else:
    print("{} NUMBER IS ODD" .format(num))
    

#Nested if ===> If statement in other if statement
number = int(input("Enter the number::"))
if(number%2 == 0):
        if(number%4 == 0):
            print("{} number divided by both 2 & 4" .format(number))
else:
    print("Sorry.. number not divide by 2 & 4")


##if-elif ladder
print("B.Tech Admmission")
rank = int(input("Enter the Rank"))
if(rank <= 1000):
    print("College1 avalible for your RANK")
elif(rank>1000 and rank <= 25000):
    print("College2 avalible for your RANK")
elif(rank>25000 and rank <= 40000):
    print("College3 avalible for your RANK")
else:
    print("No Colleges avalinle for your rank")
    


##Shorthand if ==> for single statemets

a =int(input("Enter Number"))
if a > 10 : print("{} number more than 10" .format(a))

##############################################
##Shorthand if else ==> for single statemets
#if else can be written one line when there is only one statement to be executed in both if and else
#################################################
x=10
if (x%2==0):
    print("EVEN")
else:
    print("ODD")
    
x=13 
#statementtrue if condition else statementfalse  
print("EVEN") if(x%2 == 0) else  print("ODD")  



lb =4
print("WON") if (lb == 6) else print("LOSE")

###########################################################################################################################################
#for loop  - Iterate over the sequence like -- string, list,set,tuple.
     range - used to generate range of numbers :: range(10) 
           - Returns sequence of numbers starting from 0 (by default) and increments by 1 (by default) and stops before a specified number.
             syntax:: range(start,stop,step)           
###########################################################################################################################################


###For loop
print("#############For Loop###############")

print(range(10))
numberList = [1,2,3,4,5,6,7,8,9]
for number in numberList:
    print(number)


for number in range(0,10,2):
    print(number)


name = "Phani"
for i in name:
    print(i, sep = "\t")

for item in range(10):
    print(item)

#write a program to print 100 to 1

print(range(10))
for item in range(10,0,-1):
    print(item,sep='\t')

#Write tp print your 2 chars from your name and repeat it from 1 to 10

name = input("Enter your name")
n=name[-2:]
for i in range(11,0,-1):
    print(n*i)

           

numbers = {1:"One",2:"Two",3:"Three"}
for element in numbers:
    print(element)
    print(numbers[element])
    

#findout owels & consonants in list of name
name = input("Enter your name")
vowellist = ['a','e','i','o','u']
for char in name:
    if char in vowellist:
        print(char, "- Its vowel")
    else:
        print(char,"- Its consonents")

###########################################################
ControlStatements - break      ==> Returns control out of the loop
                    continue   ==> Returns control to the begining of the loop
                    pass       ==> Used as a placeholder for future implementation of loops, functions etc.             


###########################################################

 
#if your name has vowel or not

name = input("Enter your name")
vowellist = ['a','e','i','o','u']
for char in name:
    if char in vowellist:
        print(char, '-its vowel')
        break;
     
numbers = {1:"One",2:"Two",3:"Three"}
for element in numbers:
    print(element)
    continue #Returns control to the begining of the loop; Not to next line;
    print(numbers[element])    

 
for i in range(10):
    pass  #used for future purpose
    

 
 #program to print total marks
sum =0;
L1= [50,54,64,78,54,98]
for mark in L1:
    sum= mark+sum
print("Total Marks is:: {}" .format(sum))


 
 ##################################################################################
 While -- if we everknow how many of times loops iterate
          while expression:
                statements
   
 
 
 ####################################################################################
 

  #print 1 to 10 numbers
x=1
while x < 10:
    print(x)
    x= x+1
    #print('\t')
    
###########################################################################
##Book Cricket   ---  Consider you have a book of 30 pages
                 ---  Flip the book till you get 500
                 ---  Print all the values(scores)
                 ---  Print number of flips taken to complete the 500 score
                 ---  enumerated()
                 ---  iteritem()
                 ---  items()
                 ---  zip()
                 ---  sorted()
                 ---  reversed()
###########################################################################


#random -- generate numbers randomlly 

# print(random.randint(1,30))
scoreinfo = []

score = 0;
while score <= 500:
    scorevalue=random.randint(1,30)
    score = score + scorevalue
    scoreinfo.append(scorevalue)
print("Total flips:", len(scoreinfo)) 
print("Scorevalues:",scoreinfo) 
print("Score info",score)      

###############################################################################################
function :: Group of statements design to perform specific task.
            Repeation of logic

    Syntax  :: def functionName(parameters):
                        statements
    docstring ::   describe the functionality of the function, it is a optional but a good pratice to use.
                   functionName.__doc__

    Returning from a function:: Used to return the data and exit from the function.

###############################################################################################



#write a program to check weather its a odd or even number without function

num = int(input("Enter the number:"))
print("even") if(num%2 == 0) else print("odd")

 
#write a program to check weather its a odd or even number with function 
#num1,n2,n3 = 12,13,14;
def evenOrOdd(n):
    "this is checks even or odd"#docstring
    if(n%2 == 0 ):
        print("{} number is even" .format(n))
    else:
        print("{} number is odd" .format(n))
        
evenOrOdd(19)     
evenOrOdd(12) 
evenOrOdd(14) 
print(evenOrOdd.__doc__)
print(print.__doc__)


def cubeOfNumber(n):
    n=n**3
    return n
    #return if we return any thing its return none
print(cubeOfNumber(4))##Pass value to function

#Above one example of pass by value.


##PASS BY REFERENCE   --> Pass the varible to the function which refer the address that values automatically passed.

def passByReference(mark):
    mark[3] = 80 ##put value to list not change the refernce

marks = [86,76,85,84,93,88]
passByReference(marks)##PASS the varible to function
print("Marks is {}".format(marks))




def passByReference(mark):
    mark = [23,43,54] ## assign new values to variable refernce will change; it will break connection bw called & calling methods.

marks = [86,76,85,84,93,88]
print(passByReference(marks))##PASS the varible to function
print("Marks is {}".format(marks))


def luckyNumber(num):
    num = 20
    return num

n = 10
print("function", luckyNumber(n))
print("outside",n)

######################################################
#Default Arguments :: 
###################################################

def num(x,y=10):#y=10 is default argument
    print("x value is {} & y value is {}".format(x,y))
    
num(14,13)
num(12)


###############################################################################################
Keyword Arguments :: we can specify argument name and value together while calling a function.

################################################################################################


def bottleDetails(name, color,capacity,height):
    print("name : {}  color : {}  capacity :{} height : {}" .format(name,color,capacity,height))

#bottleDetails("Aqua","Blue",'1L','15CM')
#bottleDetails("Blue","Aqua",'1L','15CM')
bottleDetails(color="Blue",name="Aqua",capacity='1L',height='15CM')##If we have more number of arguments use argumets names to pass values to parameters. no need to follow order with argument names.


################################################################################################
Varible of arguments   ---   *args(normal arguments/Non keyword arguments)
                       ---   **Kwargs(Keyword Arguments) ==> Used to pass variable number of arguments.         
                                 
                             If we don't know function howmany arguments its can handle by varible arguments.  

################################################################################################


##Normal arguments
def fun1(*args):
    li = []
    for i in args:
        li.append(i)
    print(li)    
       

fun1(12,13,43,123,41,22)



##multi of given number

def multiply(*args):
    mult = 1 #defult value
    for number in args:
        mult = mult * number
    return mult

result  = multiply(2,5,6,12)
print("RESULT IS ::", result)


def multiply(start,*args):
    mult = start
    for number in args:
        mult = mult * number
    return mult

result  = multiply(2,2,5,6,12)##first argument pass to 
print("RESULT IS ::", result)

##Variable number of keyword arguments

def bottleDetails(**kwargs):
    for key, value in kwargs.items():
        print("key {} : value {} " .format(key,value))

bottleDetails(color="Blue",name="Aqua",capacity='1L',height='15CM')



################################################################################
Generators   ---   Generator Function  :: If the body of function contains yield then that function becomes generator function.



                   Generator Object ::  Generator function return a generator object. you can get values from generator object either by calling next
                                        (__next__) method or using a for loop.


###################################################################################

def coconetCalaries(number):
    cal = number * 19
    return cal  ## retun cal and exit from function not print next line.
    print("SUPER")
    
    
calaries = coconetCalaries(2)
print("Calaries Is:", calaries)



def coconetCalaries(number):
    cal = number * 19
    yield cal  ## yield suspends function execution and sends value back to the caller and then resumes where it left off.
    print("SUPER")
    
    
calaries = coconetCalaries(2)
for i in calaries:
    print(i)

#print("Calaries Is:", calaries)


##########################################################
Anonymous function :: (lamda) unknown function 
                        we can use lambda for creating anonymous function.
                        
                        
                        
filter     ::   filters the list based on some condition
                filter(function,iterable)
Map        ::  iterates through all items in the list and returns list with new items.
                map(function,iterable)
                
Reduce     ::  returns a single value.
                reduce(function,sequence,initial)
                
#NOTE      ::  All of these methods takes a function and list

                

###########################################################



def cube(num):
    return num*num*num
    
print(cube(4))


result = (lambda num:num*num*num)(3)
print(result)



def isEven(num):
    return num%2 == 0
    
numbers = [23,32,43,22,12,53,25,46]
result = filter(isEven,numbers)
print(list(result))



##use Anonymous function using lambda

numbers = [23,32,43,22,12,53,25,46]
result = filter(lambda num:num%2 == 0,numbers)
print(list(result))


def isEven(num):
    return num.upper()
    
numbers = ["phani","deep","challa"]
result = map(isEven,numbers)
print(list(result))



numbers = ["phani","deep","challa"]
result = map(lambda num:num.upper(),numbers)
print(list(result))


def addAll(a,b):
    return a+b

numbers = [12,32,23,43,54]
result = reduce(addAll,numbers)
print(result)
 


numbers = [12,32,23,43,54]
result = reduce(lambda a,b:a+b,numbers)
print(result)



numbers = [12,32,23,43,54]
result = reduce(lambda a,b:a+b,numbers,10)
print(result)




##########################################################################################################
OOPS  ---   Object Oriented Programing System
           
Class ---  Blueprint to create objects.

class className:
    #attributes
    #functions

Object ---  Anything has state and behaviour called object.       

Constractor  -- its one kind of method and put defalut values to the object. 
                it is a special method given by python itself.(__init__(self)).
                constructor automatically created when we create a class but its not be visible to you.
                
destrator    -- __del__()   

#################################################################################
Inheritance -----

        class childclass(parentclass):
            #statements


mutple inheritance - python supports multiple inheritance




################################################################################## 


################################################################################################################


id =1
color = "red"
capacity = "1L"
height = "15CM"

def wash():
    print("Washing")
    
def setCap():
    print("setCap")
   
def fillWater():
    print("fill Water")



 
#Creating class
class Bottle:
    "This class is used to create a bottle"
    #properties or states
    #static/class variable
    companyName = "TATA"
    
    #Create COntructor
    def __init__(self,color,capacity):
        print(self)
        self.color = color;
        self.capacity=capacity;
        print("Contructor")
        print(self.color)
        
    def __del__(self):
        print("destructor")
    #functions or Behavious
    def wash(self):
        print(self)
        print("Washing")
    
    def setCap(self):
        print("setCap")
   
    def fillWater(self):
        print("fill Water")    
        
        
#Create object or instantiate object
print(Bottle.companyName)
rel = Bottle("green","1.5L")
print(rel.color)
rel1 = Bottle("green","1.5L")
print(rel1.color)
#print(bottle.id)
#print(rel.id,rel.color,rel.capacity,rel.height, sep = '\t')

rel.wash()
rel.setCap()
rel.fillWater()
 
print("#########  CHILD CLASS CREATION  #################")
 
class CopperBottle(Bottle):
    def __init__(self,color,capacity):
        #Bottle.__init__(self,color,capacity)#Pass the arguments from child class to parent class.
        super().__init__(color,capacity)#if we use super to call parent class no need keep the self. 
        print("Child Constrator")
    def mornWater():
        print("Morning Water")


print(CopperBottle.companyName) 

CopperBottle("YELLOE","2L")
#cp1.wash() 
#print(cp1.color)

##Howto know the parent of any class
#class.__bases__
#How to know parent of class from an object
#object.__class__.__bases__

print(Bottle.__bases__)
print(CopperBottle.__bases__)
print(CopperBottle.__class__.__bases__)


############################################################
Encapsulation ---process of wrapping code and data together into single unit.
                prevent accendital modification of data.
                
Access modifier - public::access any where in class
                  private ::only access with in class(__)
                  protected - access by subclasses(_)


############################################################




############################################################
Polymorphism-- same name but differrent form/functionality

##In python we don't have methode overloading concept. but it support funname(self, *args)
Methode overloading --  Two methods have same name but diffrrent number of parameters .
Methode overriding  -- if child class had same method as declared in the parent class then it is called method overriding.

############################################################

##Exception handling


class join:
    
    def members(self):
        try:
            members = ["PHANI","DEEP","CHALLA"]
            print(members[3])
        except:
            errorinfo = sys.exc_info()
            print(errorinfo[0],errorinfo[1])

j1 = join()
j1.members()


##File handling
Type of operation 
==========================
*Read only(r)
*Write only(w)
*Read and Write(r+)
*Write and Read(W+)
*Append Only(a)
*Append and Read(a+)


Open file - open(filename,accesmode)
==============================


name=input("Enter Your name:")
file = open("PythonWrite.txt","w")
file.write("WELCOME {} TO UK!!!" .format(name))



file = open("PythonWrite.txt","r")
print(file.read())


file = open("PythonWrite.txt","a")
file.write(" Enjoy thr Days")
file.close()

"""

##With statement ==> file automatically close.

with open("PythonWrite.txt","r") as file:
    print(file.read())


