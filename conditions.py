# Conditional Statements in Python:


# Tasks:

'''1. Create a variable called age and store the value 25.
Use an if statement to check whether the age is greater than or equal to 18.
If the condition is true, print: Eligible to Vote'''

age = 25
if age >= 18:
    print('Eligible to Vote')


'''2. Create a variable called temperature and store the value 35.
Use an if statement to check whether the temperature is greater than 30.
If the condition is true, print: Hot Weather'''

temp = 35
if temp > 30:
    print('Hot Weather')


'''2. Create a variable called marks and store the value 40.
Use an if else statement:
• If marks are greater than or equal to 50, print Pass
• Otherwise, print Fail'''


marks = 40
if marks >= 50:
    print('Pass')
else:
    print('Fail')


'''3. Create a variable called balance and store the value 5000.
Use an if else statement:
• If balance is greater than or equal to 10000, print Sufficient Balance
• Otherwise, print Low Balance'''

balance = 5000
if balance >= 10000:
    print('Sufficient Balance')
else:
    print('Low Balance')


'''5. Create a variable called score and store the value 92.
Use if elif else statements:
• If score is greater than or equal to 90, print Grade A
• Else if score is greater than or equal to 70, print Grade B
• Otherwise, print Grade C'''

score = 92
if score >= 90:
    print('Grade A')
elif score >= 70:
    print('Grade B')
else:
    print('Grade C')


'''6. Create a variable called salary and store the value 60000.
Use if elif else statements:
• If salary is greater than or equal to 100000, print High Salary
• Else if salary is greater than or equal to 50000, print Medium Salary
• Otherwise, print Low Salary'''

salary = 60000
if salary >= 100000:
    print('High Salary')
elif salary >= 50000:
    print('Medium Salary')
else:
    print('Low Salary')


'''7. Create a variable called number and store any whole number.
Use an if else statement to check:
• If the number is even, print Even Number
• Otherwise, print Odd Number
Hint: Use the modulus operator (%) with 2.'''

num = 25
if num % 2 == 0:
    print('Even Number')
else:
    print('Odd Number')


'''8. Create a variable called username and store the value admin.
Use an if else statement:
• If username is equal to admin, print Access Granted
• Otherwise, print Access Denied'''

username = 'admin'
if username == 'admin':
    print('Access Granted')
else:
    print('Access Denied')


'''9. Create a variable called attendance and store the value 80.
Use an if else statement:
• If attendance is greater than or equal to 75, print Allowed in Exam
• Otherwise, print Not Allowed in Exam'''

attendence = 80
if attendence >= 75:
    print('Allowed in Exam')
else:
    print('Not Allowed in Exam')


'''10. Create a variable called purchase_amount and store the value 12000.
Use if elif else statements:
• If purchase_amount is greater than or equal to 20000, print 20% Discount
• Else if purchase_amount is greater than or equal to 10000, print 10% Discount
• Otherwise, print No Discount'''

purchase_amount = 12000
if purchase_amount >= 20000:
    print('20% Discount')
elif purchase_amount >= 10000:
    print('10% Discount')
else:
    print('NO Discount')



''' some other conditions '''
num = int(input('Enter your number:'))
if num > 0:
    if num % 2 == 0:
        print('Positive Even Number')
    else:
        print('Positive Odd Number')
elif num < 0:
    print('Negative number')
else:
    print('zero')

#####

username = input('Enter Username:')
password = input('Enter Password:')
if username == 'admin' and password == 'python123':
    print('Access Granted')
elif username == 'admin':
    print('Wrong password')
else:
    print('Access Denied')
