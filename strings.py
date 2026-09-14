# task- Strings

'''1. Create a string variable called name and store your own name inside it.
      Print the variable on the screen.'''

name = 'joseph'
print(name)

'''2. Create a variable called city and store your city name inside it.
      Convert the text into uppercase using the upper() method and print the result.'''

city = 'Birmingham'
print(city.upper())

'''3. Create a variable called country and store your country name inside it.
      Convert the text into lowercase using the lower() method and print the result.'''

country = 'ENGLAND'
print(country.lower())

'''4. Create the following sentence:
      sentence = "Python is difficult"
      Replace the word "difficult" with "easy" and print the updated sentence.'''

 
sentence = 'Python is difficult'
print(sentence.replace('difficult', 'easy'))
print(sentence)

sentence = 'Python is difficult'
sentence = sentence.replace('difficult', 'easy')
print(sentence)

'''5. Create two variables:
      first_name = "Mark”
      last_name = "Wood"
      Combine both variables into a single variable called full_name using string concatenation.
      Print the full name.'''

first_name = 'Mark'
last_name = 'Wood'
full_name = first_name +" "+ last_name
print(full_name)

name1 = f'{first_name} {last_name}'
print(name1)

name2 = " " .join([first_name, last_name])
print(name2)

print(f'my first name is {first_name} and last name is {last_name}')
print('my names is %s ' % name2)
print('my name is {}'.format(name2))


'''6. Create a variable called favorite_food and store your favorite food name inside it.
      Print the text in uppercase and lowercase.'''

favorite_food = 'Biriyani'
print(favorite_food.upper())
print(favorite_food.lower())

'''7. Create the following sentence:
      message = "Data Analysis is boring"
      Replace the word "boring" with "interesting" and print the updated sentence.'''

message = 'Data Analysis is boring'
message = message.replace('boring','interesting')
print(message)

'''8. Create variables for your first name and your profession.
      Use an f-string to display a sentence like:
      My name is Mark and I am a Data Analyst'''

first_name = 'Joseph'
job = 'Data'
job = f"{job} Analyst"
print(job)
print(f"Im {first_name} and I am a {job}")
# print('Im {} and I am a {}'.format(first_name, job))
# print('Im %s and Im a %s' %(first_name, job))


'''9. Create the following variables:
      product = "Laptop"
      price = 85000
      Use an f-string to display:
      The price of Laptop is 85000'''

product = 'Laptop'
price = 85000
print(f"The price of the {product} is {price}.")

'''10. Create your own mini introduction using strings and f-strings. 
       Include:
       Your Name
       Your City
       Your Favorite Skill
       Display everything in one professional sentence.'''

name = 'Josep Vinod Raj'
f_skill = 'Data Science and Analytics'
print(f"My name is {name}, I live in {city}, and my favorite skill is {f_skill}")



