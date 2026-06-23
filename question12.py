import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,20,15,25,30]

fig, ax = plt.subplots(2,2, figsize=(8,6))

ax[0,0].plot(x,y)
ax[0,0].set_title("Line Plot")

ax[0,1].scatter(x,y)
ax[0,1].set_title("Scatter Plot")

ax[1,0].bar(x,y)
ax[1,0].set_title("Bar Chart")

ax[1,1].hist(y)
ax[1,1].set_title("Histogram")

plt.suptitle("All Plots")
plt.tight_layout()
plt.show()
