import pandas as pd

df = pd.read_csv("auto.csv")

#1
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df.to_csv("cleaned_auto.csv", index=False)
print("\n1. Cleaned and updated CSV file saved as 'cleaned_auto.csv'.")

#2️
most_expensive = df.loc[df["price"].idxmax(), "company"]
print(f"\n2. Most Expensive Car Company: {most_expensive}")

#3️
toyota_cars = df[df["company"].str.lower() == "toyota"]
print("\n3. Toyota Cars Details:")
print(toyota_cars)

#4️
car_counts = df["company"].value_counts()
print("\n4. Total Cars by Company:")
print(car_counts)

#5️
highest_priced_cars = df.loc[df.groupby("company")["price"].idxmax()]
print("\n5. Highest Priced Car from Each Company:")
print(highest_priced_cars[["company", "price"]])

#6️
avg_mileage = df.groupby("company")["average-mileage"].mean()
print("\n6. Average Mileage by Company:")
print(avg_mileage)

#7️
df_sorted = df.sort_values(by="price", ascending=False)
print("\n7. Cars Sorted by Price:")
print(df_sorted)