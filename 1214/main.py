class Student:
    def __init__(self, name, id, major):
        self.name = name
        self.id = id 
        self.major = major
        self.subject =[]

    def addsubject(self):
        return self

st1 = Student("大A", "S001", "資工")
st2 = Student("小b", "S002", "電機")

if __name__ == "__main__":
     print(st1.name,st1.id,st1.major)
     print(st2.name,st2.id,st2.major)