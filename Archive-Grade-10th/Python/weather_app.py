import requests

print("Weather App")
city = input("Enter city: ")

API_KEY = "ad57615f39c0c5574dd6e9a5bee1025b"
url = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + API_KEY + "&units=metric"

data = requests.get(url).json()

if data["cod"] != "404":
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print("Temp:", temp, "C")
    print("Condition:", desc)
else:
    print("City not found")

