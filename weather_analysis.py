import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_data.csv")

print(df)

df.plot(kind='bar')
plt.title("Weather Analysis")
plt.show()