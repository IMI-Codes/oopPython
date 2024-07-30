class Hero:
  def __init__(self) :
    self.name = None
    self.type = None #this is set by default 
    self.verse = None
    self.genre = None
  
  #setters
  def setName(self,input):
    self.name = input
  
  def setType(self,value):
    self.type = value
  #getters
  def getName(self):
    return self.name
  
  
    

    



#className.method(instance)