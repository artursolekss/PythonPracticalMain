from Person import Person

class Employee(Person):#inheritance from class Person (Employee extends Person)
    
    def __init__(self, name: str, last_name: str, date_of_birth: str,position:str) -> None:
        self.position = position
        super().__init__(name, last_name, date_of_birth)
    
    def __str__(self) -> str:#override the function from the super-class/parent class
        return super().__str__() + "\nPosition : " + self.position