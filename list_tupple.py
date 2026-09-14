# Lists and Tuples in Python

'''1. Create a list called fruits containing the following items:
• Apple
• Banana
• Mango
Print the complete list.'''

fruits = ['Apple', 'Banana', 'Mango']
print(fruits)


'''2. Create a list called colors with the following values:
• Red
• Blue
• Green
Print:
• The first item
• The second item'''

colors = ['Red', 'Blue', 'Green']
print(colors[0])
print(colors[1])

print(colors[0], colors[1])
print(f"first item: {colors[0]}, second iten: {colors[1]}")


'''3. Create a list called cities containing:
• London
• Leicester
• Manchester
Add a new city:
• Cardiff
Print the updated list.'''

cities = ['London', 'Leicester', 'Manchester']
cities.append('Cardiff')
print(cities)
cities.remove('Cardiff')
print(cities)

cities += ['Cardiff']
print(cities)

del cities[0]
print(cities)
cities.insert(0, 'London')
print(cities)

'''4. Create a list called students containing:
• Mark
• Kate
• David
Remove Kate from the list.
Print the updated list.'''

students = ['Mark', 'Kate', 'David']
# del students[1]
students.remove('Kate')
print(students)


'''5. Create the following list: numbers = [10, 20, 30, 40]
Print:
• The complete list
• The first item
• The last item'''

numbers = [10, 20, 30, 40]
print(numbers)
print(numbers[0])
print(numbers[3])
# print(numbers[0:2])
# print(numbers[::-1])
# print(numbers[1:])


'''6. Create a list called animals containing:
• Cat
• Dog
• Horse
Add:
• Lion
Remove:
• Dog
Print the final list.'''

animals = ['Cat', 'Dog', 'Horse']
# animals[1]= 'Lion'
animals.append('Lion')
animals.remove('Dog')
print(animals)


'''7. Create a tuple called weekdays containing:
• Monday
• Tuesday
• Wednesday
• Thursday
• Friday
Print the tuple.'''

weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
print(weekdays)
print(type(weekdays))

'''8. Create a tuple called countries containing:
• England
• Soctland
• Wales
Print:
• The first country
• The second country'''

countries = ('England', 'Scotland', 'Wales')
print(countries[0])
print(countries[1])
# print(countries[0:2])


'''9. Create the following list: shopping_cart = ["Milk", "Bread", "Eggs"]
Add:
• Butter
Remove:
• Bread
Print the updated shopping cart'''

shopping_cart = ["Milk", "Bread", "Eggs"]
# shopping_cart[1] = 'Butter'
shopping_cart.append('Butter')
shopping_cart.remove('Bread')
print(shopping_cart)

'''10. Create the following: products = ["Laptop", "Mouse", "Keyboard"] prices = (85000, 1500,
3000)
Print:
• The products list
• The prices tuple
• The first product
• The second price'''

products = ['Laptop', 'Mouse', 'Keyboard']
prices = (85000, 1500, 3000)
print(products)
print(prices)
print(products[0])
print(prices[1])
# print(products,'\n', prices)
# print(products[0],'\n', prices[1])





