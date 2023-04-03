from dataclasses import dataclass
#Task 1
# class Car:
#     def __init__(self,make,model,year) -> None:
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return "Make : " + self.make + ", Model : " + self.model + ", Year : " + str(self.year)


# car = Car("Audi","A3",2020)
# print(car.get_info())

# @dataclass
# class Car:
#     make:str
#     model:str
#     year:int

# car = Car("Audi","A3",2020)
# print(car)

#Task 2
# @dataclass
# class Rectangle:
#     width:float
#     height:float

#     def area(self):
#         return self.width * self.height
#     def perimeter(self):
#         return 2 * (self.height + self.width)

# rectangle = Rectangle(10,20)
# print(rectangle.area())
# print(rectangle.perimeter())

#Task 3
# @dataclass
# class BankAccount:
#     account_number:str
#     balance:float
#     owner_name:str
    
#     def deposit(self,amount):
#         self.balance += amount
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Not possible to withdraw, because the amount exceeds the balance")
#         else:
#             self.balance -= amount

# bank_account = BankAccount("LV834343",20000,"Jack Peterson")
# print(bank_account)
# bank_account.deposit(100)
# print(bank_account)
# bank_account.withdraw(400)
# print(bank_account)
# bank_account.withdraw(40000)

# #Task 4
# @dataclass
# class Address:
#     street:str
#     city:str
#     country:str
#     house_number:int

#     def get_info(self) -> str:
#         return self.street + " " + str(self.house_number) + ", " + self.city + ", " + self.country

# @dataclass
# class Person:
#     name:str
#     age:int
#     address:Address

#     def get_info(self):
#         return "Name : " + self.name + ";Age : " + str(self.age) + ";Address : " + self.address.get_info()

# address = Address("Brivibas","Riga","Latvia",1)
# person = Person("Janis",25,address)
# print(person.get_info())

#Task 5

# @dataclass
# class Animal:
#     name:str
#     species:str

#     def speak(self):
#         return "Ohoo"

#Task 6
# @dataclass
# class Vehicle:
#     make:str
#     model:str
#     year:int
    
#     def get_info(self):
#         return "Make : " + self.make + ", Model : " + self.model + ", Year : " + str(self.year)
    

# @dataclass
# class Car(Vehicle):
#     number_of_doors:int

# @dataclass
# class Truck(Vehicle):
#     width:float
#     max_width:float

#     def max_cargo_width(self):
#         return self.max_width - self.width

# car = Car("Audi","A3",2020,4)
# print(car)

# truck = Truck("Volvo","V4",2020,10000,15000)
# print(truck.max_cargo_width())

#Task 7

# @dataclass
# class Address:
#     street:str
#     city:str
#     country:str
#     house_number:int

#     def get_info(self) -> str:
#         return self.street + " " + str(self.house_number) + ", " + self.city + ", " + self.country

# @dataclass
# class Person:
#     name:str
#     age:int
#     address:Address

#     def get_info(self):
#         return "Name : " + self.name + ";Age : " + str(self.age) + ";Address : " + self.address.get_info()

# @dataclass
# class Student(Person):
#     study_field:str

# @dataclass
# class Teacher(Person):
#     subject:str

# #Task 8
# import json

# key = "age"
# with open("Persons.json","r") as f:
#     persons = json.load(f)["persons"]

# persons.sort(key=lambda person:person[key])

# with open("Persons.json","w") as f:
#     json.dump({"persons":persons},f)

# #Task 9
# with open("Students_Grades.csv","r") as f:
#     students_grades = f.readlines()

# averages = list()
# for student_line in students_grades[1:]:
#     columns = student_line.replace("\n","").split(";")
#     name = columns[0]
#     sum_grade = 0
#     for grade in columns[1:]:
#         sum_grade += int(grade)
#     averages.append([name,sum_grade/(len(columns)-1)])

# csv_output = students_grades[0].replace("\n","")
# for student in averages:
#     csv_output += "\n" + student[0] + ";" + str(student[1])

# with open("Student_average.csv","w") as f:
#     f.write(csv_output)

#Task 10

import csv

lines = list()
with open("Students_Grades.csv","r") as csvfile:
    students_grades_csv = csv.reader(csvfile,delimiter=";")
    for student in students_grades_csv:
        lines.append(student)

student_grades = lines[1:]
student_grades.sort(key= lambda student:student[0])


print(lines)
# with open("Students_Grades.csv","w") as csvfile:
#     writer = csv.writer(csvfile,delimiter=";")
#     writer.writerow(lines[0])
#     writer.writerows(student_grades)