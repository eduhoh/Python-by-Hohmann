
import requests
import sys
import json

#Define Latitude and Longitude to get weather info:
lat = "37.742828"
long = "-25.680588"
unit = "si"
APIkey = "TypeHereYourAPIkey"

#API URL
url = f"https://api.pirateweather.net/forecast/{APIkey}/{lat},{long}?&units={unit}]"

try:
    print("Capturing data from pirateweather.net ...  \n")
    r = requests.get(url, timeout=5)
    #print(r)
except:
	print("Failed")
	sys.exit()

#Translating JSON
report = json.loads(r.text)

#Converting Temperature
temp = int((((float(report['currently']['temperature'])) - 32)*5)/9)

summary = report['currently']['summary']
icon = report['currently']['icon']

#Output

print("\n \n Current weather in Ponta Delgada, Portugal:")
print(temp, "°C")
print("Condition:",summary)
#print(icon)
match icon:
    case "cloudy":
        print("\U0001F325")
    case "partialy-cloudy":
        print("\U0001F324")
    case "clear":
        print("\U0001F323")
    case "rain":
        print("\U0001F326")
        
print("\n \n")

