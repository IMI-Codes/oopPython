#Classes 

class Human :
  def __init__(self):
    self.gender = None
    self.age = None
    self.firstName = None
    self.lastName  = None
    self.otherName = None
   
  def setGender(self,value):
    gender = value.lower()
    if gender == 'm' or 'male':
      self.gender = 'Male'
    elif gender == 'f' or 'female':
      self.gender = 'Female'
    else:
      print('Not a Valid Gender')
    
  def setName(self,value):
    fullName = value
    if " " in fullName:
      names = fullName.split(' ')
      if names.len == 3:
        self.firstName = names[0]
        self.lastName = names[1]
        self.otherName = names[2]
      elif names.len == 2:
        self.firstName = names[0]
        self.otherName = names[1]
    elif " " not in fullName:
      self.firstName = fullName
  def setAge(self,value):
    try:
      age = int(value)
    except:
      print('Not a valid age enter a number between 1 - 200')
    self.age = age 