import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data for study hours (X) and exam grade (Y)
data = {
    "Study Hours": [1, 1, 2, 2, 3, 3, 4, 4],
    "Exam Grade": ["Fail", "Pass", "Fail", "Pass", "Fail", "Pass", "Fail", "Pass"],
    "Count": [10, 5, 8, 12, 4, 16, 2, 43]
}

# Create DataFrame
df = pd.DataFrame(data)

# Add total students
total_students = df["Count"].sum()

# Calculate joint probabilities
df["P(X,Y)"] = df["Count"] / total_students

# Create pivot table for heatmap
pivot_table = df.pivot(index="Study Hours", columns="Exam Grade", values="P(X,Y)")

# Plot heatmap of joint probabilities
plt.figure(figsize=(8, 5))
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Joint Probability Distribution: Study Hours vs Exam Grade")
plt.ylabel("Study Hours")
plt.xlabel("Exam Grade")
plt.tight_layout()
plt.show()
