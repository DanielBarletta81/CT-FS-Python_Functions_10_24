###The aim of this assignment is to build a basic calculator 
#that can perform addition, subtraction, multiplication, and division.

#Task 1: Create functions for each arithmetic operation.

#Task 2: Use inputs to ask the user what operation they want to perform, 
# and what numbers they want to use.

#Task 3: Ensure your code can handle division by zero and other potential errors.
#  So if you divide by 0, there is error handling set up to prevent an error
#  from showing in the console.


#task 1
def add(x, y):
   result =  x + y
   print(result)

def subtract(x, y):
 result =  x - y
 print(result)

def multiply(x, y):
   result =  x * y
   print(result)

def divide(x, y):
   result =  x / y
   print(result)

#Task 2 

x = int(input('Enter first number: '))

operation_choice = input('Choose your operation: add/subtract/multiply/divide ')

y = int(input('Enter next number: '))

   

if operation_choice == 'add':
    add(x, y)
elif operation_choice == 'subtract':
    subtract(x, y)
elif operation_choice == 'multiply':
    multiply(x, y)
elif operation_choice == 'divide':
    # Task 3
    if y == 0:
       print('Error! Can not divide by 0.')
    else:
       divide(x, y)
else:
   print('The was an error with input.')

    

    