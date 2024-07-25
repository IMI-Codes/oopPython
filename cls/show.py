class Show:
  def __init__(self):
    self.showName = None
    self.firstAired = None
    self.genre = None
    self.type = None
    self.Alias = {"name of show":self.showName,"date first aired":self.firstAired,"genre":self.genre,"show type":self.type}
  def setValue(self,valueName,value):
    print(f"List of Value:\n  1. Name of Show:{self.showName}\n 2. Date First Aired:{self.firstAired}\n 3. Movie Genre : {self.genre}\n 4. Show Type:{self.type}\n Which Attributes do you want to set or update?\n Enter The Attribute Name or Number\n")
    userInput = input()
    
    
class Anime(Show):
  def __init__(self):
    super().__init__(self)


demonSlayer = Anime()

