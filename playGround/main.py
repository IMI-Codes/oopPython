""" fullName = "ishima manasseh ishima"
myNames = fullName.split(' ')

nameContainer = list()

for name in myNames:
  converted = name.capitalize()
  nameContainer.append(converted)


delimiter = " "
finalName = delimiter.join(nameContainer)
print(finalName) """

name = input("Enter Name:\n")
print(f"Hello {name}")