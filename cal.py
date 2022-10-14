import math
import datetime

#greet the user
def greeter():
    now = datetime.datetime.now()
    hour = now.hour
    if hour >=0 and hour <12:
        print('Good morning, choose function and follow the instructions')
    elif hour >12 and hour < 18:
        print ('Good afternoon, choose function and follow the instructions')
    else:
        print ('Good evening, choose function and follow the instructions')

greeter ()
# docstring

#Addition
def addition(x, y): 
    print (x+y)
    
#Subtraction
def subtraction (x, y):
    print (x -y)
    
#multiplication
def multiplication (x,y):
    print(x * y)
    
#division
def division (x , y):
    print (x/y)

#first number
f_num = input('Enter your first number')
s_num = input('Enter your second number')

print("""
      1. addition
      2. subtraction
      3. multiplication
      4. division
      """)
    
# i want to collect the user operator
user_option = input('enter your choice:')

#check for the operator
if int(user_option) == 1:
    addition(int(s_num), int (f_num))
elif int(user_option) == 2:
    subtraction (int(s_num), int(f_num))
elif int(user_option) == 3:
    multiplication (int(s_num),int (f_num))
elif int(user_option) == 4:
    division (int(s_num), int(f_num))
else:
    print('follow the rule')
  