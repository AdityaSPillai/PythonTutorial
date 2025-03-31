import pandas as pd

df = pd.read_csv("student.csv")

#1
average_cgpa = df["CGPA"].mean()
print("\n1. Average CGPA of Students:", round(average_cgpa, 2))

#2
high_cgpa_students = df[df["CGPA"] > 9]
print("\n2. Students with CGPA > 9:\n", high_cgpa_students)

#3
cse_high_cgpa = df[(df["Branch"] == "CSE") & (df["CGPA"] > 9)]
print("\n3. CSE Students with CGPA > 9:\n", cse_high_cgpa)

#4
max_cgpa_student = df[df["CGPA"] == df["CGPA"].max()]
print("\n4. Student with Maximum CGPA:\n", max_cgpa_student)

#5
branch_avg_cgpa = df.groupby("Branch")["CGPA"].mean()
print("\n5. Average CGPA of Each Branch:\n", branch_avg_cgpa)