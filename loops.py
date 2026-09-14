# Loops in Python

'''1. Use a for loop with range(5).
Print all numbers from 0 to 4.'''

for i in range(5):
    print(i)

'''2. Use a for loop with range(1, 6).
Print all numbers from 1 to 5.'''

for n in range(1,6):
    print(n)


'''3. Create a list called colors containing:
• Red
• Blue
• Green
Use a for loop to print all colors one by one.'''

colors = ['Red', 'Blue', 'Green']
for c in colors:
    '''if c == 'Blue':
        continue'''
    print(c)


'''4. Create a list called cities containing:
• London
• Manchester
• Leicester
Use a for loop to display all city names.'''

cities = ['London', 'Manchester', 'Leicester']
for c in cities:
    print(c)


'''5. Create a variable called count and assign the value 1.
Use a while loop to print numbers from 1 to 5.'''

count = 1
while count <= 5:
    print(count)
    count += 1


'''6. Create a variable called number and assign the value 2.
Use a while loop to print: 2 4 6 8 10
Hint: Increase the value by 2 during every iteration'''

print("differnt operation")
number = 2
while number <= 10:
    print(number)
    number += 2

'''7. Create a list called fruits containing:
• Apple
• Banana
• Mango
• Orange
Use a for loop to print each fruit'''

fruits = ['Apple', 'Banana', 'Mango', 'Orange']
for f in fruits:
    print(f)

'''8. Use a for loop with range(1, 11).
Print all numbers from 1 to 10.'''

for i in range(1,11):
    print(i)


'''9. Create a variable called counter and assign the value 5.
Use a while loop to print numbers from 5 down to 1.'''

counter = 5
while counter > 0:
    print(counter)
    counter -= 1


'''10. Create the following list: subjects = ["Math", "Physics", "Computer", "English"]
Use a for loop to display all subjects one by one.'''

subjects = ['math', 'Physics', 'Computer', 'English']
for s in subjects:
    print(s)


''' finding largest number'''
numbers = [13,46,75,45,98,27,35,65,77]

largest = numbers[0]
for n in numbers:
     if n > largest:
         largest = n
print('Largest nuber is', largest)

# simple way

print(max(numbers))

###########################################