# Mathematical Operations in Python:

'''1. Create two variables:
num1 = 15
num2 = 5
Print the result of addition between both variables.'''

num1 = 15
num2 = 5
print(num1 + num2)
print(sum([num1, num2]))

'''2. Create two variables:
a = 20
b = 8
Print the result of subtraction.'''

a = 20
b = 8
print(a-b)


'''3. Create two variables:
price = 12
quantity = 4
Print the multiplication result.'''

price= 12
quantity = 4
print(price * quantity)

'''4. Create two variables:
total_marks = 500
subjects = 5
Print the division result.'''

total_marks = 500
subjects = 5
print(total_marks/subjects)


'''5. Create the following variables:
number1 = 25
number2 = 7
Print:
  Addition
  Subtraction
  Multiplication
  Division '''

number1 = 25
number2 = 7
print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 / number2)

'''6. Use the modulus operator to find the remainder:
17 % 4
Print the output.'''

reminder = 17 % 4
print(reminder)

'''7. Create a variable called number and store any whole number inside it.
Use the modulus operator to check whether the number is even or odd.
Hint:
  Even numbers give remainder 0 when divided by 2. '''

num = 10
if num % 2 == 0:
    print('even number')
else:
     print('odd number')

# user input
'''num = int(input('Enter number:'))
if num % 2 == 0:
    print('even number')
else:
     print('odd number')'''


'''8. Use the exponent operator to calculate:
3 raised to the power 4
Print the output.'''

print(3**4)
print(pow(3,4))


'''9. Use floor division to divide:
22 // 5
Print the result.'''

res = 22 // 5
print(res)

import math
print(math.floor(22/5))

'''10. Create the following variables:
monthly_salary = 75000
bonus = 15000
Calculate and print:
• Total Salary
• Salary after subtracting tax of 5000
• Double Salary using multiplication
• Salary divided equally into 12 months'''

monthly_salary = 75000
bonus = 15000

total_salary = monthly_salary + bonus
sal_after_Tax = total_salary - 5000
double_sal = total_salary * 2
sal_per_month = total_salary / 12

print('total salary', total_salary)
print(f'salary after tax is {sal_after_Tax}')
print('Double salary would be %.2f' %(double_sal))
print('salary per month is {}'.format(sal_per_month))

#################################




