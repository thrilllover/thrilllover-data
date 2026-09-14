# Dictionaries in Python:

'''1. Create a dictionary called student with the following information:
• name = Allen
• age = 22
• course = Python
Print the complete dictionary.'''

student = {'name':'Allen', 'age': 22, 'course':'Python'}
print(student)
print(type(student))


'''2. Create a dictionary called employee with the following data:
• name = David
• department = HR
• salary = 50000
Print:
• The employee name
• The department'''

employee = {'name': 'David', 'department': 'HR', 'salary': 50000}
print(employee['name'])
print(employee['department'])
# print(employee.items())
# print(employee.values())
# print(employee.keys())
# print(list(employee.values())[:2])

'''3. Create a dictionary called product with the following values:
• product_name = Laptop
• price = 85000
• brand = Dell
Add a new key:
• color = Black
Print the updated dictionary.'''

product = {'product_name': 'Laptop', 'price': 85000, 'brand': 'Dell'}
product['color'] = 'Black'
# product.update({'color': 'Black'})
print(product)


'''4. Create a dictionary called car with the following information:
• brand = Toyota
• model = Corolla
• year = 2020
Update the year value to 2024.
Print the updated dictionary.'''

car = {'brand': 'Toyota', 'model': 'Corolla', 'year': 2020}
print(car)
# car['year'] = 2024
car.update({'year':2024})
print(car)


'''5. Create the following dictionary: student = { "name": "Sara", "age": 21, "city": "London" }
Print:
• The complete dictionary
• The student name
• The city'''

student = {'name': 'Sara', 'age': 21, 'city': 'London'}
print(student)
print(student['name'])
print(student['city'])


'''6. Create a dictionary called mobile with the following values:
• brand = Samsung
• model = S24
• price = 250000
Add:
• color = Silver
Update:
• price to 240000
Print the final dictionary'''

mobile = {'brand': 'Samsung', 'model': 'S24', 'price': 250000}
# mobile.update({'color': 'Silver', 'price': 240000})
mobile['color'] = 'Silver'
mobile.update({'price':240000})
print(mobile)


'''7. Create a dictionary called book with the following information:
• title = Python Basics
• author = John Smith
• pages = 350
Print:
• The book title
• The author name'''

book = {'title': 'Python Basics', 'author': 'John Smith', 'pages': 350}
print(f"Book name is {book['title']} and the author is {book['author']}")


'''8. Create a dictionary called university with the following values:
• name = Oxford University
• country = England
• ranking = 1
Update the ranking value to 2.
Print the updated dictionary'''

university = {'name': 'Oxford University', 'country': 'England', 'ranking': 1}
university.update({'ranking': 2})
# university['ranking'] = 2
print(university)


'''9. Create the following dictionary: customer = { "name": "Allen", "city": "London",
"membership": "Gold" }
Add:
• phone = 44001234567
Print the updated customer dictionary.'''

customer = {'name': 'Allen', 'city': 'London', 'membership': 'Gold'}
customer['phone'] = 44001234567
# customer.setdefault('phone', 44001234567)
print(customer)


'''10. Create the following dictionary: company = { "name": "Tech Solutions", "employees": 150,
"location": "London" }
Print:
• The company name
• The number of employees
Update:
• employees to 200
Print the updated dictionary'''

company = {'name': 'Tech Solutions', 'employees': 150, 'location': 'London'}
print(company['name'], company['employees'])
company.update({'employees': 200})
print(company)

###############################