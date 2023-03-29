import json

class PersonsFile:
    persons:list

    def __init__(self,filename) -> None:
        self.filename = filename
    
    def merge(persons_file1,persons_file2):
        merged = persons_file1.persons + persons_file2.persons
        persons_file1.persons = merged
        persons_file2.persons = merged

class Persons_Json(PersonsFile):
    def load_persons(self):
        with open(self.filename,"r") as f:
            persons_file = json.load(f)
            self.persons = persons_file["persons"]
            f.close()
    def generate_file(self):
        with open(self.filename,"w") as f:
            json.dump({"persons":self.persons},f)

class Persons_Csv(PersonsFile):
      def parse_csv_persons(self,person_lines,header_line=True):
          self.persons = list()
          if header_line:
              start_i = 1
          else:
              start_i = 0
          for i in range(start_i,len(person_lines)):
              person_csv_line_list = person_lines[i].split(";")
              person = {"name":person_csv_line_list[0],
                        "last_name":person_csv_line_list[1],
                        "age":int(person_csv_line_list[2])}
              self.persons.append(person)

      def load_persons(self):
        with open(self.filename,"r") as f:
            self.parse_csv_persons(f.readlines())
            f.close()
      def generate_csv(self,header_line=True):
        delim = ";"
        filelines = list()

        if header_line == True:
            filelines.append("First Name" + delim + "Last Name" + delim + "Age")#header line

        for person in self.persons:
            line = person["name"] + delim + person["last_name"] + delim + str(person["age"])
            filelines.append("\n" + line)
        return filelines
      def generate_file(self):
          with open("Persons.csv","w") as f:
              f.writelines(self.generate_csv())

obj_json = Persons_Json("Persons.json")
obj_json.load_persons()

obj_csv = Persons_Csv("Persons.csv")
obj_csv.load_persons()

merged = PersonsFile.merge(obj_json,obj_csv)

merged_format = input("What is the file format the data needs to be merged to?(json/csv)\n")

if merged_format == "json":
    obj_json.generate_file()
elif merged_format == "csv":
    obj_csv.generate_file()