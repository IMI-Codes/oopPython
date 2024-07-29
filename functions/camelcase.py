def camelCase(value,spiltpara):
  if type(value) != str and type(spiltpara) != str:
    return 
  else:
    try:
      word = value.lower()
      spiltFrom = word.find(spiltpara)
      firstPart = word[0:spiltFrom]
      secondPart = word[spiltFrom:].capitalize()
      words = [firstPart,secondPart]
      delimter = ""
      finalWord = delimter.join(words)
      return finalWord
    except:
      print('please check your entry and try again')


  
 
