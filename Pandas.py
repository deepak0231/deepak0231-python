import pandas as pd
df = pd.read_csv(r"C:\Users\badri\OneDrive\Desktop\Data Science\Python Codes\Diabetes data.txt")
print(df.head())
print(df.tail())
print("Length of DF is", (len(df)))
print(type(df))
print("Columns are:", df.columns)