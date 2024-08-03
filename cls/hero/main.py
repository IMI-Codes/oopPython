
class Hero:
  def __init__(self) :
    self.name = None
    self.type = None 
    self.verse = None
    self.genre = None
    self.alter_ego = None
    

  
  #setters
  #remember to add validation each of the setter functions 
  def setName(self,value):
    #validation: make sure it's a valid string or if this a number convert to string
    self.name = value
  def setType(self,value):
    self.type = value
  
  def setGenre(self,value):
    self.genre = value
  
  def setVerse(self,value):
    self.verse = value
  #getters
  def getName(self):
    return self.name
  
  def getType(self):
    return self.type
  
  def getGenre(self):
    return self.genre
  
  def getGenre(self):
    return self.genre
  


#className.method(instance)