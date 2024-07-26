class Student:
  def __init__(self,name,age,grade):
    self.name = name
    self.age = age
    self.grade = grade
  def getGrade(self):
    return self.grade

class Course:
  def __init__(self,name,max_students):
    self.name = name
    self.max = max_students
    self.students = list()
    
  def addStudent(self,student):
    if len(self.student) < self.max_student:
      self.students.append(student)
      return True
    return False
  def getAverageGrade(self):
    pass
  
s1 = Student("Manasseh",25,100)
s2 = Student("Baki",18,50)
s3 = Student("Gojo",30,90)
s4 = Student("Geto",29,90)
s5 = Student("Ali",24,80)
s6 = Student("Tyson",35,75)
s7 = Student("Bond",45,98)

HTH= Course('Hand to Hand Combat',5)
Course.addStudent(s1)
Course.addStudent(s2)
Course.addStudent(s3)
Course.addStudent(s4)
Course.addStudent(s5)
