import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name":["A","B","C","D","E"],
    "Marks":[80,np.nan,90,70,np.nan],
    "City":["Jaipur","Delhi",np.nan,"Kota","Mumbai"]
})

print(df.isnull())

df["Marks"].fillna(df["Marks"].mean(), inplace=True)

df = df.dropna(subset=["City"])

print(df)
