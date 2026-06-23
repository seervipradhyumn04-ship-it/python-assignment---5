import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Marks":[75,80,85,90,70,88,92,77,83,95]
})

df["Marks"].plot(kind="hist")
plt.title("Histogram")
plt.show()

df.boxplot(column="Marks")
plt.title("Box Plot")
plt.show()

category = pd.Series([40,30,20,10],
index=["A","B","C","D"])

category.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.show()
