import pandas as pd

df = pd.read_csv("./Tutorial_5/employee.csv")

print("\nEmployee Data Preview:")
print(df.head())

#1
print("\n1. First 7 Records:")
print(df.head(7))

#2
print("\n2. Employee Names in Alphabetical Order:")
print(df["name"].sort_values().tolist())

#3
highest_paid_employee = df[df["salary"] == df["salary"].max()]["name"].values[0]
print("\n3. Employee with the Highest Salary:", highest_paid_employee)

#4
male_employees = df[df["gender"] == "Male"]["name"].tolist()
print("\n4. Male Employees:", male_employees)

#5
teams = df["team"].unique().tolist()
print("\n5. Teams Employees Belong To:", teams)