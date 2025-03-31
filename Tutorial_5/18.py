import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")

#1
print("\n1. First 10 Rows of Weather Data:\n", df.head(10))

#2
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()
print("\n2. Maximum Temperature:", max_temp)
print("   Minimum Temperature:", min_temp)

#3
low_temp_places = df[df["temperature"] < 28]["place"].unique()
print("\n3. Places with Temperature Less Than 28°C:\n", low_temp_places)

#4
cloudy_places = df[df["weather"] == "Cloudy"]["place"].unique()
print("\n4. Places with Cloudy Weather:\n", cloudy_places)

#5
weather_freq = df["weather"].value_counts()
print("\n5. Weather Frequency:\n", weather_freq)

#6
plt.figure(figsize=(10, 5))
plt.bar(df["date"], df["temperature"], color="blue")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("6. Temperature Trend Over Time")
plt.xticks(rotation=45)  
plt.show()