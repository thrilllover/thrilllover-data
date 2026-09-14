# Functions in Python

'''1. Create a function called welcome.
Inside the function, print: Welcome to Python Programming
Call the function'''

def welcome():
    print('welcome to python Programming')

welcome()


'''2. Create a function called student_message.
Inside the function, print: Keep Practicing Python
Call the function.'''

def student_message():
    print('keep practicing python')

student_message()


'''3. Create a function called greet_user that accepts one parameter called name.
Inside the function, print: Hello {name}
Call the function and pass the value: Allen'''

def greet_user(name):
    print(f'Hello {name}')

greet_user('joseph')


'''4. Create a function called display_city that accepts one parameter called city.
Inside the function, print: Welcome to {city}
Call the function and pass the value: London'''

def display_city(city):
    print('Welcome to %s' % city)

display_city('London')


'''5. Create a function called add_numbers that accepts two parameters:
• a
• b
Return the addition of both numbers.
Store the returned value inside a variable called result.
Print the result.
Use the following values: 5 and 10'''

def add_numbers(a, b):
    return a+ b

result = add_numbers(5, 10)
print(result)

'''6. Create a function called multiply_numbers that accepts two parameters.
Return the multiplication result.
Call the function using: 4 and 6
Print the output.'''

def multiply_numbers(a, b):
    return a * b

x = 4
y = 6
print(multiply_numbers(x,y))


'''7. Create a function called square_number that accepts one parameter called number.
Return the square of the number.
Call the function using: 7
Print the returned value.'''

def square_number(number):
    return number ** 2

print(square_number(7))
##

def square_num(n):
    return pow(n,2)

print(square_num(7))

## lambda function

square_n = lambda n: pow(n, 2)

print(square_n(7))

'''8. Create a function called check_even that accepts one parameter called number.
Inside the function:
• If the number is even, print Even Number
• Otherwise, print Odd Number
Call the function using: 12'''

def check_even(number):
    if number % 2 == 0:
        print('even number')
    else:
         print('odd number')
    
check_even(12)

##

def check_ev(n): print('even number' if n % 2 == 0 else 'odd number')

check_ev(5)


###############

even_check = lambda n: n % 2 ==0

print(even_check(12))

e_check = lambda n: print('even number' if n % 2 == 0 else 'odd number')

e_check(13)

'''9. Create a function called calculate_total that accepts two parameters:
• price
• quantity
Return the multiplication result.
Call the function using: price = 1500 quantity = 3
Print the returned value'''

def calculate_total( a, b):
    return a * b


price = 1500
quantity = 3
print(calculate_total(price, quantity))

###

calculate_t = lambda a, b: print(a * b)

calculate_t(price, quantity)


'''10. Create a function called introduce_student that accepts two parameters:
• name
• course
Inside the function, print: Student Name: {name} Course: {course}
Call the function using: Sara Data Analysis'''

def introduce_student (n, c):
    print(f'student name: {n}\ncourse: {c}')

introduce_student( 'Sara', 'Data Analysis')



