import numpy as np

arr = np.array([
    [10, 5, 8, 3],
    [7, 12, 9, 4],
    [6, 15, 2, 11],
    [14, 1, 13, 16]
])

print("Original Matrix:")
print(arr)

# Diagonal Elements
print("\nDiagonal Elements:")
print(np.diag(arr))

# Replace even numbers with 0
arr[arr % 2 == 0] = 0

print("\nMatrix after replacing even numbers with 0:")
print(arr)

# Index of maximum value
print("\nIndex of Maximum Value:")
print(np.argmax(arr))
