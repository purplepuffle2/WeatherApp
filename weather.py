import requests

apiKey = "677c6cd5a6b7494916627df2b6c3b154"

while True:

    city = input("\nInput a city: ")

    unitsOfMeasurement = {
        "°C" : "metric",
        "°F" : "imperial",
        "K" : "standard"
    }

    #asks for unit of measurement, exits if not C, F or K
    measurement = input("C, F or K: ").upper()
    if measurement != "C" and measurement != "F" and measurement != "K":
        print("Error: Uknown unit of measurement")
        exit()
    elif measurement == "C" or measurement == "F":
        measurement = "°" + measurement

    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey + "&units=" + unitsOfMeasurement[measurement]

    request = requests.get(url)
    json = request.json()

    #for testing
    #print(json)
    #print(json.get("cod"))

    #weather info, runs once city validity checked
    def weatherInfo():
        description = json.get("weather")[0].get("description")
        print("Today's forcast is", description)

        temp = json.get("main").get("temp")
        tempFeels = json.get("main").get("feels_like")
        print("The temperature is", str(temp) + measurement + " but feels like", str(tempFeels) + measurement)

        #tempMin = json.get("main").get("temp_min")
        #print("The minimum temperature is", str(tempMin) + "C")

        #tempMax = json.get("main").get("temp_max")
        #print("The maximum temperature is", str(tempMax) + "C")

    #tests if city is valid
    if json.get("cod") == "404":
        print("Error: Unknown city")
    else:
        weatherInfo()



