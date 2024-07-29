""" fullName = "ishima manasseh ishima"
myNames = fullName.split(' ')

nameContainer = list()

for name in myNames:
  converted = name.capitalize()
  nameContainer.append(converted)


delimiter = " "
finalName = delimiter.join(nameContainer)
print(finalName) """

name = "Manasseh"
age = "22"
info = tuple()
name,age = info
delimter = ""
final = delimter.join(info)
print(final)