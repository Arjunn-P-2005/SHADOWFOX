import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]
data = [10, 20, 20, 30, 30, 30, 40]

# ==========================================================
# =================== MATPLOTLIB SECTION ===================
# ==========================================================

# 1. Line Plot
plt.figure()
plt.plot(x, y)
plt.title("Line Plot - Matplotlib")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# 2. Scatter Plot
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot - Matplotlib")
plt.show()

# 3. Bar Chart
plt.figure()
plt.bar(categories, values)
plt.title("Bar Chart - Matplotlib")
plt.show()

# 4. Histogram
plt.figure()
plt.hist(data, bins=4)
plt.title("Histogram - Matplotlib")
plt.show()

# 5. Box Plot
plt.figure()
plt.boxplot(data)
plt.title("Box Plot - Matplotlib")
plt.show()

# 6. Pie Chart
plt.figure()
plt.pie(values, labels=categories, autopct='%1.1f%%')
plt.title("Pie Chart - Matplotlib")
plt.show()


# ==========================================================
# ===================== SEABORN SECTION ====================
# ==========================================================

sns.set(style="whitegrid")

# 1. Line Plot
plt.figure()
sns.lineplot(x=x, y=y)
plt.title("Line Plot - Seaborn")
plt.show()

# 2. Scatter Plot
plt.figure()
sns.scatterplot(x=x, y=y)
plt.title("Scatter Plot - Seaborn")
plt.show()

# 3. Bar Chart
plt.figure()
sns.barplot(x=categories, y=values)
plt.title("Bar Chart - Seaborn")
plt.show()

# 4. Histogram
plt.figure()
sns.histplot(data, bins=4)
plt.title("Histogram - Seaborn")
plt.show()

# 5. Box Plot
plt.figure()
sns.boxplot(y=data)
plt.title("Box Plot - Seaborn")
plt.show()


print("Visualization Comparison Completed Successfully!")