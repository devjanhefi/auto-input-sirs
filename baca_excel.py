import pandas as pd

df = pd.read_excel("sample RL5.xlsx")

data = df.iloc[3:]

row = data.iloc[23]   # ganti baris yang mau dicek

for i, value in enumerate(row):
    print(i, "=", value)