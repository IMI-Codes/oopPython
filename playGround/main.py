from playGround.inputs import *
from cls import Human

h1 = Human()
h1.setName(getName())
h1.setGender(getGender())
h1.setAge(getAge())
values= h1.showHuman()

