# from Person import Person#from Person file import Person class
from Employee import Employee
from Student import Student
from Person import calculate_age
from Person import Person
from Obsolete import Obsolete

# # person_obj = Person("Arturs","Olekss","01111997",25)#create the object Person

# # # print_person(person_obj)
# # print(person_obj)#the function __str__ is called
# # Person.print_number_of_functions()
# # # print("The Persons are " + Person.get_genys_species())
# # print("The Persons are " + Person.species)

# # person_obj1 = Person("Janis","Ozolins","01011998",25)

# # print("Sum of ages : " + str(Person.count_total_age([person_obj,person_obj1]) ))

employee = Employee("Arturs","Olekss","15111997","Programmer")
student  = Student("Jack","Peterson","16032003","Master")
print(calculate_age(employee))
print(calculate_age(student))

person_obj1 = Person("Janis","Ozolins","01011998")
print(isinstance(person_obj1,Obsolete))
# print(employee)

# class Empty:
#     pass

# obj = Empty()
# obj.param1 = "12121"
# obj.param2 = "212121"

# print(obj.param1)
# print(obj.param2)