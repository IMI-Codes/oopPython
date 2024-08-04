from transport.transport import vehicle
#anything that flies will fall under the plane call
class plane(vehicle):
  def __init__(self):
    super().__init__()
    self.mediumOfTransport = "Air"
