import pandas as pd

data = {
    "SN": [1, 2, 3],
    "Name": ["Dennis Ritchie", "James Gosling", "Bjarne Stroustrup"],
    "Country": ["USA", "Canada", "Denmark"],
    "Contribution": ["C Programming Language", "Java Programming Language", "C++ Programming Language"],
    "Year": [1972, 1995, 1983]
}

df = pd.DataFrame(data)

print("Data Frame:")
print(df)