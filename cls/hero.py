class Hero:
  def __init__(self) :
    self.name = None
    self.type = None
    self.verse = None
    self.genre = "Fiction"
    
  def setValue(self,attrName,attrValue):
    self.attrName = attrValue
    print(f"You set {attrName} with the value {attrValue} ")
  def setName(self,value):
    self.name = value
  def setType(self,value):
    self.type = value
  def setVerse (self,value):
    self.verse = value
  def showValues(self):
    return {"name":self.name,
            "typeOfHero":self.type,
            "universe":self.verse,
            "Genre":self.genre
            }
    
class AnimeHero(Hero):
  def __init__(self):
    super().__init__()
    self.type = 'Anime'
    
class MovieHero(Hero):
  def __init__(self):
    super().__init__()
    self.type = "Movie"
    
class ActualHeroes(Hero):
  def __init__(self):
    super().__init__()
    self.genre = "Real Life"
    

A1 = AnimeHero()
A1.setName('Baki')
A1.showValues()