from abc import ABC, abstractmethod
class Sport(ABC):
  @abstractmethod
  def playing(self):
    print("playing")
  
class contactSport(Sport):
  def __init__(self,name):
    super().__init__(name)
    self.name = name    
    
s1 = contactSport('Boxing')
print(s1.name)