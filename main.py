#BASE URL: https://superheroapi.com/api/
#Access Token: c4b7360a717f1fc2bc5f364dd2b453d2

import requests
#make this with javascript too 
baseUrl = "https://superheroapi.com/api/c4b7360a717f1fc2bc5f364dd2b453d2/search"
heroName = input(f"Enter Hero:\n")
finalUrl = f"{baseUrl}/{heroName}"
getHero = requests.get(url=finalUrl)
data = getHero.json()
print(data)