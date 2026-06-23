import pandas as pd

df = pd.DataFrame({
    "Name":["A","B","C","D","E","F","G","H","I","J"],
    "Age":[18,19,20,21,18,19,20,21,22,18],
    "Marks":[85,72,91,65,78,88,70,95,60,82],
    "City":["Jaipur","Delhi","Mumbai","Pune","Kota","Jaipur","Delhi","Mumbai","Pune","Kota"]
})

print(df.head())
print(df.describe())

print(df[df["Marks"]>75])

print(df.sort_values("Marks", ascending=False))
