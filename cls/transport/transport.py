class vehicle:
  def __init__(self):
    self.mediumOfTransport = None
    self.examples = dict()
    self.primaryFunction = None
    self.types = dict()

"""
build a function that goes the internet maybe an api and
fetches random pictures and names of the transport that and stores them for future
also can delete any one that does not match 
"""

#anything that moves on land will fall under the car class
class car(vehicle):
  def __init__(self):
    super().__init__()
    self.mediumOfTransport = "Land"
   
#anything that flies will fall under the plane call
class plane(vehicle):
  def __init__(self):
    super().__init__()
    self.mediumOfTransport = "Air"

class boat(vehicle):
  def __init__(self):
    super().__init__()
    self.mediumOfTransport = 'Water'


class bike(car):
  def __init__(self):
    super().__init__()
    
    