class film:
  def __init__(self,name,filmType):
    self.movieName = name.lower()
    self.typeofMovie = filmType.lower()
  
  def setReleaseYear(self,year):
    self.yearOfRelease = year
  
  def getReleaseYear(self):
      return self.yearOfRelease
    
#creating an empty class or scafolding a class
class martial_art:
  pass




m1 = film('Batman','movie')
m2 = film('Peaky Blinders',"series") 
m3 = film('Attack on Titan','Anime')

m1.setReleaseYear(2012)
m2.setReleaseYear(2015)
