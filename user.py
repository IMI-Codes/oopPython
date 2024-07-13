from myModule.main import greet
from myModule.main import Athlete

print(greet('Manasseh'))


class Boxer(Athlete):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.sport = 'Boxing'
  def showValues(self):
    return {"name":self.name,"age":self.age,"sport":self.sport}

b1 = Boxer('Manasseh',25)

values = b1.showValues()

print(values)