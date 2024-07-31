def checkTypeString(para):
  if type(para) == str:
    return para
  elif type(para) != str:
    #variables to check conditions and store user Input
    options = ["yes","y",1,"n","no",0]
    confirm = options[0:3]
    reject = options[3:]
    finalValue = None
    
    #getting user Input
    userInput = input(f"Do you what to convert {para} to a suitable format to be stored?\nEnter Yes(Y)/No(N)\n")
    
    
    
    if type(userInput) == str:  
      convertedUserInput = userInput.lower()
      finalValue = convertedUserInput
    elif type(userInput) == int:
      finalValue = userInput
    
    if finalValue in options and finalValue in confirm:
      try:
        converted = str(para)
        return converted
      except:
        print("cannot convert")
    elif finalValue in options and finalValue in reject:
      exit
    elif finalValue not in options:
      print("Not a Valid option")
      
    
      
   
      
  

