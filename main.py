#object oriented programming

class Human:
  def __init__(self,age,name):
    self.gName = name
    self.actualAge = age
  
  def greeting(self):
    return f"Hello I'm {self.gName}"
  
  def set_country(self,country):
    self.originCountry = country
  def get_country(self):
    return self.originCountry

man = Human(35,'Manasseh')
man.set_country('Nigeria')
print(f"{man.greeting()},I was born in {man.get_country()}")