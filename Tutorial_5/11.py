import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./Tutorial_5/sales.csv")
print(" Sales Data Preview:")
print(df.head())


#1)
plt.figure(figsize=(8,5))
plt.scatter(df["month_number"], df["toothpaste"], color="red", marker="o", label="Toothpaste Sales")
plt.xlabel("Month")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales Per Month")
plt.legend()
plt.grid(True)
plt.show()


#2)
plt.figure(figsize=(8,5))
plt.bar(df["month_number"] - 0.2, df["facecream"], width=0.4, color="blue", label="Face Cream Sales")
plt.bar(df["month_number"] + 0.2, df["facewash"], width=0.4, color="green", label="Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title(" Face Cream & Face Wash Sales Per Month")
plt.xticks(df["month_number"])
plt.legend()
plt.show()


#3)
total_sales = {
    "Face Cream": df["facecream"].sum(),
    "Face Wash": df["facewash"].sum(),
    "Toothpaste": df["toothpaste"].sum(),
    "Bathing Soap": df["bathingsoap"].sum(),
    "Shampoo": df["shampoo"].sum(),
    "Moisturizer": df["moisturizer"].sum(),
}

plt.figure(figsize=(8,5))
plt.pie(total_sales.values(), labels=total_sales.keys(), autopct="%1.1f%%", startangle=140, colors=["blue", "green", "red", "purple", "orange", "cyan"])
plt.title(" Total Sales Distribution for the Year")
plt.show()