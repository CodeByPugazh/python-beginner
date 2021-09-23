birth_year = input("Enter your birth year: ")

print(type(birth_year))

age = 2021 - int(birth_year) #Type casting to int

print('Your age is: ' + str(age)) #Type casting to string then print