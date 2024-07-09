class Hero: 
  def __init__(self,name) :
    self.name = name
    if(self.name.find(' ') != 0):
      space = self.name.find(' ')
      self.firstName = self.name[0:space]
      self.otherName = self.name[space:]
  def set_attr(self,attribute):
    self.heroAttribute = attribute
    

hero1 = Hero('Baki Hanma')
