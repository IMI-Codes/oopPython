from main import Hero
class ActualHeroes(Hero):
  def __init__(self):
    super().__init__()


Ali = ActualHeroes()
print(Ali.genre)