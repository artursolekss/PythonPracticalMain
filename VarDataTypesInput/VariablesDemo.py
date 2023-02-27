# name = "Arturs"
# print(name)
# name = "Janis"
# print(name)
# age = 25
# print(age)

# name = 30
# print(name)

# Variables are case-sensitive in Python
# variable = "323232"
# Variable = 1111

# print(Variable)

# Will trigger the error, because the types are different
# x = 5
# y = "9"
# sum = x + y
# print(sum)

# x = 5
# y = "9"
# sum = str(x) + y #str does the conversion to string
# print(sum)

# x= -5
# y = 5
# sum = x + y
# print(sum)

# x = 5 + 3j
# y = 8 + 2j
# sum = x + y
# print(sum)

# name = "Arturs"
# lastname = "Olekss"
# fullname = "Mr. " + name + " " + lastname
# birthyear = 1997
# currentyear = 2023
# age = currentyear - birthyear
# print("Hello " + fullname + ", you are " + str(age) + " years old")

# ac = 4 + 6j
# bc = 5 - 3j
# sum = ac + bc
# print("Real part of sum " + str(sum.real))
# print("Imaginary part of sum " + str(sum.imag))

# text = "here is my text"
# print(text.imag)  #error, because strings do not have such property

# a = 5.6565
# b = 0.32
# sum = a + b
# print(sum)

# a = 0.2
# b = 0.1
# sum = a + b
# print(sum)
# print(sum - 0.3 < 0.0001)

# print("Enter your name:")
# name = input()

# print("Enter your last name:")
# lastname = input()

# print("Enter your year of birth")
# # birthyearStr = input()
# # birthyear = int(birthyearStr)
# birthyear = int(input())

# currentyear = 2023
# age = currentyear - birthyear

# print("Hello " + name + " " + lastname, ", you are " + str(age) + " years old")

# print("Enter you name and lastname")

name,lastname,yearofbirthstr = input("Enter you name, lastname and birth year").split()

birthyear = int(yearofbirthstr)
age = 2023 - birthyear
print("Hello " + name + " " + lastname + ", you are " + str(age) + " years old")
