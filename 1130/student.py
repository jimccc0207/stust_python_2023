class Student:
    schoolName ="南台科技大學"
    schooladdress = "南台街1號"
    
    def __init__(self, department, director, name, id, credit, gpa):         
        self.department = department
        self.director = director
        self.name = name
        self.id = id
        self.credit = credit
        self.gpa = gpa

    @property
    def student_name(self):
        print(f'"{self.name}" was accessed')
        return self.name

    @student_name.setter
    def student_name(self,value):
       print(f'"{self.name}" is now "{value}".')
       self.name = value

    @student_name.deleter
    def student_name(self):
        print(f'"{self.name}" was deleted')
        del self.name

if __name__ == "__main__":
        student1 =Student("John Doe", 20, "S12345", 3.5)
        print(student1.student_name)
        student1.student_name = "Petrer Pan"
        del student1.student_name
        print(student1.student_name)
    
    
    
    
    
    
    
    
    
def getschoolName(self):
        return self.schoolName
def setschoolName(self, value):
        self.schoolName = value

def getdepartment(self):
        return self.department
def setdepartment(self, value):
        self.department = value
    
def getdirector(self):
        return self.director
def setdirector(self, value):
        self.director = value
    
def getname(self):
        return self.name
def setname(self, value):
        self.name = value
    
def getid(self):
    return self.id
def setid(self, value):
        self.id = value
    
def getaddress(self):
        return self.credit
def setschooladdress(self, value):
        self.schooladdress = value
    
def getcredit(self):
        return self.credit
def setcredit(self, value):
       self.credit = value
    
def getgpa(self):
        return self.gpa
def setschool(self, value):
        self.school = value
    
st1 = Student("CSIE","洪國均", "張晉嘉","4B0G0139", 60, 4.00)#建立類別為student的物件st1
print(st1.getschoolName())#呼叫副函式getschoolName()
print(st1.getid())#呼叫副函式getid()