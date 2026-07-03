import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=13.08&longitude=80.27&current_weather=true"

response = requests.get(url)
data = response.json()

temperature = data["current_weather"]["temperature"]
windspeed = data["current_weather"]["windspeed"]

weather_data = {
    "Temperature": [temperature],
    "Wind Speed": [windspeed]
}

df = pd.DataFrame(weather_data)
df.to_csv("weather_data.csv", index=False)

print(df)