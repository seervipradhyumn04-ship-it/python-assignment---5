import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": np.random.randint(20,50,50),
    "Salary": np.random.randint(20000,100000,50),
    "Department": np.random.choice(["HR","IT","Sales"],50),
    "Experience": np.random.randint(1,15,50)
})

sns.scatterplot(data=df, x="Age", y="Salary",
hue="Department")
plt.show()

sns.heatmap(df[["Age","Salary","Experience"]].corr(),
annot=True)
plt.show()

sns.barplot(data=df, x="Department", y="Salary")
plt.show()
