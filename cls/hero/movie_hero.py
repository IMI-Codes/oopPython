from main import Hero
class MovieHero(Hero):
  def __init__(self):
    super().__init__()
    self.type = "Movie"