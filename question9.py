import matplotlib.pyplot as plt

subjects = ["Math","Sci","Eng","CS","AI"]
marks = [80,85,78,90,88]

plt.plot(subjects, marks, marker="o", label="Marks")
plt.title("Marks Trend")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid()
plt.show()

students = ["A","B","C","D","E"]
marks2 = [75,88,92,70,85]

plt.bar(students, marks2)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid()
plt.show()
