import pandas as pd
import matplotlib.pyplot as plt

data = {
    "rollno": [201, 202, 203, 204, 205],
    "name": ["Olivia", "Liam", "Sophia", "Noah", "Emma"],
    "place": ["San Francisco", "Seattle", "Boston", "Denver", "Atlanta"],
    "mark": [90, 87, 93, 80, 89]
}

df = pd.DataFrame(data)

df.to_csv("stud.csv", index=False)
print("'stud.csv' created successfully!")

df = pd.read_csv("stud.csv")

#a)
print("File Contents:")
print(df)

#b)
df.set_index("rollno", inplace=True)
print("\nData with rollno as index:")
print(df)

#c)
print("\n Name & Mark:")
print(df[["name", "mark"]])

#d)
df_sorted_by_name = df.sort_values(by="name")
print("\nRollno, Name, Mark sorted by Name:")
print(df_sorted_by_name[["name", "mark"]])

#e)
df_sorted_by_mark = df.sort_values(by="mark", ascending=False)
print("\nRollno, Name, Mark sorted by Mark (Descending):")
print(df_sorted_by_mark[["name", "mark"]])

#f)
average_mark = df["mark"].mean()
median_mark = df["mark"].median()
mode_mark = df["mark"].mode()[0] 

print("\nStatistics:")
print(f"Average Mark: {average_mark}")
print(f"Median Mark: {median_mark}")
print(f"Mode Mark: {mode_mark}")

#g)
min_mark = df["mark"].min()
max_mark = df["mark"].max()

print("\n Min & Max Marks:")
print(f"Minimum Mark: {min_mark}")
print(f"Maximum Mark: {max_mark}")

#h)
variance_mark = df["mark"].var()
std_dev_mark = df["mark"].std()

print("\n Variance & Standard Deviation:")
print(f"Variance of Marks: {variance_mark}")
print(f"Standard Deviation of Marks: {std_dev_mark}")

#i)
plt.hist(df["mark"], bins=5, color='skyblue', edgecolor='black')
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram of Marks")
plt.show()

#j)
df.drop(columns=["place"], inplace=True)
print("\n Data after removing 'place' column:")
print(df)