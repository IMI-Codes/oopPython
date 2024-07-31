
class Hero:
  def __init__(self) :
    self.name = None
    self.type = None #this is set by default 
    self.verse = None
    self.genre = None
  
  #setters
  def setName(self,input):
    pass
    
  
  def setType(self,value):
    self.type = value
  #getters
  def getName(self):
    return self.name
  
johnWick = Hero()
johnWick.setName(1)

    



#className.method(instance)