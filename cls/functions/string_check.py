def checkTypeString(para):
  if type(para) == str:
    return para
  elif type(para) != str:
    try:
      converted = str(para)
      return converted 
    except:
      print("Not a string a cannot convert to string")
  

myList  = None

checkTypeString(myList)