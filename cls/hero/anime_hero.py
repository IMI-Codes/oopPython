from main import Hero

class AnimeHero(Hero):
  def __init__(self):
    super().__init__()
    self.type = "Anime"
    
a1 = AnimeHero()

