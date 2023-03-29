# class Person:
#     pass
#     # name:str
#     # last_name:str
#     # date_of_birth:str

# ao = Person()
# ao.name = "Arturs"
# ao.last_name = "Olekss"
# ao.date_of_birth = "01011990"

# print(ao.name)
# print(ao.last_name)
# print(ao.date_of_birth)

# pers2 = Person()
# pers2.name = "Janis"
# pers2.last_name = "Liepins"
# pers2.date_of_birth = "01061991"

# print(pers2.name)
# print(pers2.last_name)
# print(pers2.date_of_birth)
from Additional.Date import Date
from Obsolete import Obsolete

class Person(Obsolete):

    species = "Homo sapiens"
    def __init__(self,name:str,last_name:str,date_of_birth:str,
               #   age:int
                 ) -> None:#constructor
         self.name = name
         self.last_name = last_name
         self.date_of_birth = Date(date_of_birth)
     #     self.age = age
    
    def __str__(self) -> str:#we can ovveride generic functions
         return "Name : " + self.name + "\nLast Name : " + self.last_name + "\nDate of birth : " + str(self.date_of_birth)
    
    def print_number_of_functions():
         print("There are 2 functions in the class Person")
    
    def get_genys_species():
         return Person.species
#     def count_total_age(person_list:list) -> int:
#          age = 0
#          for person in person_list:
#               age += person.age
#          return age
    

# def print_person(person:Person):
#      print("Name : " + person.name)
#      print("Last Name : " + person.last_name)
#      print("Date of birth : " + person.date_of_birth)

# person_obj = Person() - error, because the parameters are missing
# person_obj = Person("Arturs","Olekss","01111997",25)#create the object Person

# # print_person(person_obj)
# print(person_obj)#the function __str__ is called
# Person.print_number_of_functions()
# # print("The Persons are " + Person.get_genys_species())
# print("The Persons are " + Person.species)

# person_obj1 = Person("Janis","Ozolins","01011998",25)

# print("Sum of ages : " + str(Person.count_total_age([person_obj,person_obj1]) ))

def calculate_age(person:Person):
     age = 2023 - person.date_of_birth.year
     return age


