#anything that moves on land will fall under the car class
from transport.transport import vehicle
class car(vehicle):
  def __init__(self):
    super().__init__()
    self.mediumOfTransport = "Land"