import numpy as np

a = np.linspace(1,10,5)
b = np.zeros(5)
c = np.ones(5)

result = np.vstack((a,b,c))

print(result)
